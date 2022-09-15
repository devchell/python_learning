# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa

'''
from math import pow, sqrt
ad = float(input('Digite o valor do cateto adjacente: '))
op = float(input('Digite o valor do cateto oposto: '))
hip1 = pow(ad, 2) + pow(op, 2)
hip2 = sqrt(hip1)
print(f'O valor da hipotenusa é {hip2:.2f}')
'''

from math import hypot
ad = float(input('Digite o valor do cateto adjacente: '))
op = float(input('Digite o valor do caceto oposto: '))
print(f'O valor da hipotenusa é {hypot(ad, op)}')