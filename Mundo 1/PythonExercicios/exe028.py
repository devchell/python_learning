# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar.
# descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário acertou ou errou.
from random import randint
nu = int(input('Digite um número de 0 a 5: '))
print('')
nc = randint(0, 5)
if nu == nc:
    print('Parabéns! Você acertou')
else:
    print('Você errou! Tente novamente')
print(f'Número escolhido: {nc}')
