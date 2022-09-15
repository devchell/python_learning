# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

'''
n = str(input('Digite um número (4 digitos): ')).strip()
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')
'''

n = int(input('Digite um número: '))
print('')
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}')
print('')
print(f'Dezena: {d}')
print('')
print(f'Centena: {c}')
print('')
print(f'Milhar: {m}')