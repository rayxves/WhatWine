import pandas as pd;
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

arquivo = pd.read_csv("./assets/wine_dataset.csv")

arquivo['style'] = arquivo['style'].replace('white', 1)
arquivo['style'] = arquivo['style'].replace('red', 0)

alvo = arquivo['style']
preditora = arquivo.drop('style', axis = 1)

preditora_treino, preditora_teste, alvo_treino, alvo_teste = train_test_split(preditora, alvo, test_size=0.3)

modelo = ExtraTreesClassifier()
modelo.fit(preditora_treino, alvo_treino)

resultado = modelo.score( preditora_teste, alvo_teste)
print("Acurácia: ", resultado)

previsoes = modelo.predict(preditora_teste[400:403])
print("Previsões: ", previsoes)