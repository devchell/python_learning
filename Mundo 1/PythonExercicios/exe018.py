# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

'''
#(Em radianos)
from math import cos, sin, tan
a = float(input('Digite o ângulo: '))
print(f'O ângulo digitado foi {a}º, tendo os seguintes resultados: ')
print(f'Seno: {sin(a):.2f}')
print(f'Cosseno: {cos(a):.2f}')
print(f'Tangente: {tan(a):.2f}')
'''

#(Em ângulo)
from math import cos, sin, tan, radians
a = float(input('Digite o ângulo: '))
print(f'O ângulo {a:.0f}º tem os valores seguintes: ')
print(f'Seno: {sin(radians(a)):.2f}')
print(f'Cosseno: {cos(radians(a)):.2f}')
print(f'Tangente: {tan(radians(a)):.2f}')