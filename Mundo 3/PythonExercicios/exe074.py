# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print('Os números sorteados foram: ', end='')
for i in n:
    print(f'{i} ', end='')
print(f'\nO maior valor foi: {max(n)}')
print(f'O menor valor foi: {min(n)}')