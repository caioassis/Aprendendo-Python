# Programa que cadastra as informações do funcionário, faz um sorteio de um vale compras (trabalhando com random e listas)
# E exibe em seguida essas informações cadastradas em uma mensagem.

from datetime import datetime
from random import randint
import random

print('\n-------- Seja bem vindo (a) a nossa empresa! --------')

# Entrada de dados do usuário
nome = input('\nNome do funcionário: ')
idade = int(input('Idade do funcionário: '))
data_registro = datetime.now()  # Pega a data em tempo real

valor_cartao = ['R$50,00', 'R$100,00', 'R$120,00', 'R$250,00']
# Sorteia de forma aleatoria um valor da lista
valor_cartao = random.choice(valor_cartao)
data_aniversario = datetime.strptime(
    input('Data de aniversário: '), '%d/%m/%Y')

# Exibe uma mensagem de boas vindas contendo as informações que foram registradas pelo usuario.
mensagem = (f'\nOlá {nome}, seu registro foi feito com sucesso no dia {data_registro.day}/{data_registro.month}/{data_registro.year}. \nParabens houve um sorteio e voce ganhou um vale compras no valor de {valor_cartao}.\n')

print(mensagem)
