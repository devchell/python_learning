# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
p = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end='')
        p += 1
    else:
        print('\033[31m', end='')
    print(f'{i}\033[0m ', end='')
print('')
if p == 2:
    print(f'O número {n} pode ser divisível por {p} valores, por isso é um número primo!')
else:
    print(f'O número {n} pode ser divisível por {p} valores, por isso não é um número primo!')