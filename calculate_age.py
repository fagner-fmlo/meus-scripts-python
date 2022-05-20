'''
O script captura o nome, ano de nascimento, ano atual e a cidade. 
Com isso subtrai do ano atual, o ano de nascimento que é passado como parâmetro pelo usuário. 
No final apresenta uma mensagem concatenando os parâmetros fornececidos.
'''
from datetime import date

nome = input('Digite aqui o seu nome: ')
ano_nascimento = input('Digite aqui o seu ano de nascimento: ')
ano_atual = date.today().year
idade = int(ano_atual) - int(ano_nascimento)
cidade = input('Digite aqui a sua cidade: ')
print('O ' + nome + ' tem ' + str(idade) + ' anos de idade e mora em ' + cidade + '.')
