import logging
import pandas as pd
from pathlib import Path
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from helpers import tratamento_descricoes


parent_path = Path(__file__).parents[0]

logger = logging.getLogger("model-spam")
logger.setLevel(logging.INFO)

logger.info("Importando os dados")
dados = pd.read_csv(parent_path / "dataset/dados.csv")

logger.info("Aplicando tratamento/limpeza nos dados")
dados.dropna(inplace=True)
tratamento_texto = tratamento_descricoes.TratamentoTexto()


def tratamento_strings(text):
    texto = str(text)
    texto = texto.lower()
    texto = tratamento_texto.remove_pontuacao(texto)
    texto = tratamento_texto.remove_space(texto)
    texto = tratamento_texto.remove_space_duplicado(texto)
    return texto


dados["Message_tratada"] = dados["Message"].apply(tratamento_strings)

logger.info("Divisão da base em treino e teste: 80% treino e 20% teste")
features = dados["Message_tratada"]
target = dados["Category"]

x_train, x_test, y_train, y_test = train_test_split(
    features, target, test_size=0.20, random_state=10, stratify=target
)

logger.info("Criando pipeline para treino e teste do modelo")
logger.info("Modelo considerado: Naive Bayes")
pipeline_model_nb = Pipeline(
    [
        ("vect", TfidfVectorizer(ngram_range=(1, 1), analyzer="word")),
        ("modelo_nb", MultinomialNB()),
    ]
)

logger.info("Treinando o modelo")
model = pipeline_model_nb.fit(x_train, y_train)

logger.info("Aplicando modelo na base de teste")
model_test = model.predict(x_test)

logger.info("Verificando desempenho do modelo")
desempenho_model = precision_recall_fscore_support(y_test, model_test, average="macro")

logger.info(
    "Precision/Recall/F-score do modelo NB na base de teste é: {resultado}".format(
        resultado=desempenho_model
    )
)

logger.info("Salvando o modelo treinando")
filename = parent_path / "model/spam-nb-model.pkl"
pickle.dump(model, open(filename, "wb"))
