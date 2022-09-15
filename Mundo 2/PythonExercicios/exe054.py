# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda 
# não atingiram a maioridade e quantas já são maiores.
from datetime import date
ma = 0
mn = 0
for i in range(1, 7):
    ano = int(input(f'Digite o ano de nascimento da pessoas {i}: '))
    idade = date.today().year - ano
    if idade >= 18:
        ma += 1
    elif idade < 18:
        mn += 1
print(f'')
print(f'Há {ma} pessoas maiores de idade e {mn} pessoas menores de idade!')