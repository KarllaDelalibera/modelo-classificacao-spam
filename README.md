[![python](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/)

# Repositório destinado a criação de um modelo de classificação para detecção de spam

O objetivo desse pequeno projeto foi explorar a library [Streamlit](https://www.streamlit.io/) do Python. Para isso, foi desenvolvido um modelo de classificação bem simples para detecção de spam.

### Fonte de dados

Foram utilizados dados do Kaggle! Os mesmos encontra-se disponíveis [aqui](https://www.kaggle.com/team-ai/spam-text-message-classification).

### Modelagem

Para a modelagem desses dados foi utilizando o modelo de classificação Naive Bayes.

# Como utilizar

No terminal, clone o projeto:

```
git clone https://github.com/KarllaDelalibera/modelo-classificacao-spam.git
```

Dentro da pasta modelo-classificacao-spam, execute o seguinte comando no terminal:

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run app.py
```
