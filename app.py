import numpy as np
import pandas as pd
from pathlib import Path
import pickle
import streamlit as st

parent_path = Path(__file__).parents[0]


@st.cache
def carrega_dados(path):
    dados = pd.read_csv(path)
    return dados


def carrega_modelo_treinado(path):
    with open(path, 'rb') as f:
        modelo_rf = pickle.load(f)
    return modelo_rf


def predict_modelo(modelo, texto):
    predicao = modelo.predict([texto])[0]
    predicao_prob = np.round(np.max(modelo.predict_proba([texto])), 2)
    return [predicao, predicao_prob]


def main():
    df = carrega_dados(path=parent_path / 'dataset/dados.csv')
    modelo = carrega_modelo_treinado(path=parent_path / 'model/spam-nb-model.pkl')

    st.sidebar.title("Menu de opções")
    page = st.sidebar.selectbox("Selecione uma página:", ["Objetivo", "Visualização dos dados", "Predição"])

    if page == 'Objetivo':
        st.title("Modelo de detecção de Spam")
        st.markdown("### :email: Objetivo")
        st.markdown(
            "Essa é uma aplicação utilizando Streamlit e Scikit-learn para prevermos se um e-mail é spam ou não.")

        st.markdown("### :email: Informações sobre a modelagem")
        st.markdown(
            "* Dados: Os dados dessa modelagem foram extraídos do Kaggle [link](https://www.kaggle.com/team-ai/spam-text-message-classification).")
        st.markdown("* Modelagem: O modelo considerado foi um Naive Bayes.")

    elif page == "Visualização dos dados":
        st.title("Conhecendo os dados")

        st.markdown("### :game_die: Dados de estudo")
        st.dataframe(df, width=900, height=300)

        st.markdown("### :game_die: Distribuição das classes")
        classes = df.groupby(['Category']).count()
        classes.plot.bar()
        st.pyplot()
        st.markdown(
            "De 5572 mensagens, temos 4825 e-mail's classificados como normais (ham) e 747 classificados como spam.")

    elif page == "Predição":
        st.title("Prevendo se um e-mail é spam ou não")
        user_input = st.text_input('Insira um trecho do e-mail (em inglês)', '')
        resul_predicao = predict_modelo(modelo, user_input)
        st.write('O e-mail é: {pred}, com probabilidade {prob}'.format(pred=resul_predicao[0],
                                                                       prob=resul_predicao[1]))


if __name__ == "__main__":
    main()
