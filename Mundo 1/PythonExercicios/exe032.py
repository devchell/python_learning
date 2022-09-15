# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
a = int(input('Digite o ano: '))
print('')
if a%4 == 0 or a%400 == 0:
    print(f'{a} é um ano bissexto!')
else:
    print(f'{a} não é um ano bissexto!')