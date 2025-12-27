#importações necessárias
import sqlite3
import pandas as pd
import csv

#Caminho do arquivo
raw_data_path = '/content/Debenture.csv'

#Lendo o arquivo com o pandas
dF= pd.read_csv(raw_data_path, sep=';', low_memory=False)

#Criando conexão
conn1 = sqlite3.connect('debentures.db')

#Criando tabela dentro do database
dF.to_sql('Debenture',conn1,if_exists='replace',index=False)

#Consulta no sql
query = """

SELECT
 Taxa_de_venda AS tv,
Spread
 FROM Debenture
 WHERE tv IS NOT NULL
 LIMIT 10

"""

result = pd.read_sql(query,conn1)
print(result)


