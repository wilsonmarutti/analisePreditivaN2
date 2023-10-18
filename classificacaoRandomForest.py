import pandas as pd
from pymongo import MongoClient
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Conexão com o MongoDB
client = MongoClient("mongodb+srv://wilsonmarutti:6S0oLpmf8IchaNlm@cluster0.uvdvhmj.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('Cluster0')
collection = db.mycollection

dados = list(collection.find())

# Converter dados para DataFrame
data = pd.DataFrame(dados)

features = ['sexo', 'escolaridade', 'nivelCargo', 'salarioAnual']
label = 'idade'

X = data[features]
y = data[label]

# Pré-processamento de dados (codificação de variáveis categóricas)
X = pd.get_dummies(X, columns=['sexo', 'nivelCargo', 'salarioAnual', 'escolaridade'], drop_first=True)

# Divida os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicialize o modelo RandomForestClassifier
classifier = RandomForestClassifier()

# Treine o modelo com os dados de treinamento
classifier.fit(X_train, y_train)

# Faça previsões no conjunto de teste
y_pred = classifier.predict(X_test)

# Calcule a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')
