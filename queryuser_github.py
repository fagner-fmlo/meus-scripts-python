import requests
import json
import re

#usuario = input("Insira seu usuario: ")
usuario = (f"fagner-fmlo")
response = requests.get(f"https://api.github.com/users/" +usuario).json()


nome = response['name']
id = response['id']
data_criacao = response[f'created_at']
regex = re.search('\d{4}-\d{2}-\d{2}',data_criacao)
result_data = regex.group()
ftexto = f' Olá {nome} o seu ID de usuário é {id} e sua conta foi criada em {result_data}'
print(ftexto)
