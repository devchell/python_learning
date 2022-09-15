# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número: '))
if n % 2 == 1:
    print(f'Seu número ({n}) é ímpar!')
else:
    print(f'Seu número ({n}) é par')