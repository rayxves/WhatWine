# 🍷 Classificação de Vinhos

Este é um algoritmo bem simples de **Machine Learning** criado para aprender o básico sobre classificação de dados. Ele classifica vinhos como tinto (red) ou branco (white) com base em suas características químicas, utilizando o algoritmo **Extra Trees Classifier** da biblioteca `scikit-learn`.

## Tecnologias Utilizadas

- **Python 3.13**
- **Pandas** (manipulação de dados)
- **Scikit-Learn** (modelo de Machine Learning)

## 🔧 Como Executar o Código

### 1️⃣ Criar e ativar um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar as dependências

```bash
pip install pandas scikit-learn
```

### 3️⃣ Executar o script

```bash
python main.py
```

## 📊 Sobre o Dataset

O dataset `wine_dataset.csv` contém informações químicas de vinhos e sua classificação. Ele foi obtido a partir do seguinte link:
[Wine Dataset - Kaggle](https://www.kaggle.com/datasets/dell4010/wine-dataset?resource=download) 

| fixed\_acidity | volatile\_acidity | citric\_acid | residual\_sugar | chlorides | pH  | sulphates | alcohol | quality | style |
| -------------- | ----------------- | ------------ | --------------- | --------- | --- | --------- | ------- | ------- | ----- |
| 7.4            | 0.70              | 0.00         | 1.9             | 0.076     | 3.51 | 0.56      | 9.4     | 5       | 0     |
| 7.8            | 0.88              | 0.00         | 2.6             | 0.098     | 3.20 | 0.68      | 9.8     | 5       | 0     |
| 7.8            | 0.76              | 0.04         | 2.3             | 0.092     | 3.26 | 0.65      | 9.8     | 5       | 0     |
| 11.2           | 0.28              | 0.56         | 1.9             | 0.075     | 3.16 | 0.58      | 9.8     | 6       | 0     |
| 7.4            | 0.70              | 0.00         | 1.9             | 0.076     | 3.51 | 0.56      | 9.4     | 5       | 0     |

- **Coluna `style`**:
  - `0` → Vinho tinto
  - `1` → Vinho branco

## Como Funciona o Algoritmo

- O dataset é carregado e os rótulos (`red` e `white`) são convertidos em `0` e `1`.
- Os dados são separados em **preditoras** (X) e **alvo** (y).
- O conjunto de dados é dividido em **treino (70%)** e **teste (30%)**.
- Um modelo `ExtraTreesClassifier` é treinado para aprender as características dos vinhos.
- O modelo é testado e sua **acurácia** é calculada.

## Exemplo de Saída

```bash
Acurácia:  0.98
```

Isso significa que o modelo acertou **98%** das previsões 😃
