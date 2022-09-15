# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

p = input('Digite algo: ')
print(f'Seu tipo primitivo é: {type(p)}')
print(f'Só tem espaço? {p.isspace()}')
print(f'É um número? {p.isnumeric()}')
print(f'É alfabético? {p.isalpha()}')
print(f'É alfanumérico? {p.isalnum()}')
print(f'Está em maiúsculas? {p.isupper()}')
print(f'Está em minúsculas? {p.islower()}')
print(f'Está captalizada? {p.istitle()}')
