import pandas as pd
from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient("mongodb+srv://wilsonmarutti:6S0oLpmf8IchaNlm@cluster0.uvdvhmj.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('Cluster0')
collection = db.mycollection

dados = list(collection.find())

# Converter dados para DataFrame
data = pd.DataFrame(dados)

data['nome'] = data['nome'].replace('******', 'Desconhecido')
data['sobrenome'] = data['sobrenome'].replace('******', 'Desconhecido')
data['salarioAnual'] = data['salarioAnual'].astype(int)

# Agora, os dados estão no estado pré-processado
print(data)