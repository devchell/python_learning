# Crie um programa que leia um número REAL qualquer pelo telcado e mostre na tela sua porção INTEIRA
# Ex:
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6
from math import floor
n = float(input('Digite um número: '))
print(f'O número {n} tem a parte inteira {floor(n)}')
