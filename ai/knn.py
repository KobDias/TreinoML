import pandas as pd
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv') # carregando o dataset

X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values # definindo as colunas X
y = iris['species'].values # definindo coluna y, alvo da predição

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=101) # dividindo o dataset em treino e teste

knn = KNeighborsClassifier(n_neighbors=5) # instanciando o modelo KNN com 5 vizinhos
knn.fit(X_train, y_train) # treinando o modelo

joblib.dump(knn, 'knn.pkl') # salvando o modelo pre treinado em pkl