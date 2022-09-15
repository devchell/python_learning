# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
from math import fmod, modf
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if a<b+c and b<a+c and c<b+a:
    print('')
    print('Parabéns, você criou um triângulo!')
else:
    print('')
    print('Desculpe, mas você não pode criar um triângulo com esses valores')

