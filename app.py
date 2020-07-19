import numpy as np
import pandas as pd
from pathlib import Path
import pickle
import streamlit as st

parent_path = parent_path = Path(__file__).parents[0]

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
    predicao_prob = np.max(modelo.predict_proba([texto]))
    return [predicao, predicao_prob]


def main():
    df = carrega_dados(path=parent_path / 'dataset/dados.csv')
    modelo = carrega_modelo_treinado(path=parent_path / 'model/spam-nb-model.pkl')

    page = st.sidebar.selectbox("Opções:", ["Objetivo", "Visualização dos dados", "Predição"])

    if page == 'Objetivo':
        st.title("Modelo de classificação de Spam")

    elif page == "Visualização dos dados":
        st.title("Conhecendo os dados")
        st.header("Dados de estudo")

        st.dataframe(df, width=900, height=300)
        st.text('Fonte: https://www.kaggle.com/team-ai/spam-text-message-classification')

    elif page == "Predição":
        st.title("Prevendo se um e-mail é spam ou não")
        user_input = st.text_input('Insira um trecho do e-mail', '')
        resul_predicao = predict_modelo(modelo, user_input)
        st.write('O e-mail é: {pred}, com probabilidade {prob}'.format(pred=resul_predicao[0],
                                                                       prob=resul_predicao[1]))


if __name__ == "__main__":
    main()

# streamlit run app.py
