# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120
n = int(input('Digite um número: '))
i = n
f = 1 # Nulo da multiplicação (Fatorial)
print(f'Calculando {n}! = ', end='')
'''
while i > 0:
    print(i, end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
    i -= 1
print(f)
'''
for i in range(i, 0, -1):
    print(i, end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
    i -= 1
print(f)
