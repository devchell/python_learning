# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
n1 = float(input('Digite o valor 1: '))
n2 = float(input('Digite o valor 2: '))
n3 = float(input('Digite o valor 3: '))
'''
if n1 > n2 > n3:
    print(f'Os valores do MAIOR para o MENOR é: ')
    print(f'{n1}, {n2}, {n3}')
elif n1 > n3 > n2:
    print(f'Os valores do MAIOR para o MENOR é: ')
    print(f'{n1}, {n3}, {n2}')
elif n2 > n1 > n3:
    print(f'Os valores do MAIOR para o MENOR é: ')
    print(f'{n2}, {n1}, {n3}')
elif n2 > n3 > n1:
    print('Os valores do MAIOR para o MENOR é:')
    print(f'{n2}, {n3}, {n1}')
elif n3 > n1 > n2:
    print(f'Os valores do MAIOR para o MENOR é: ')
    print(f'{n3}, {n1}, {n2}')
else:
    print(f'Os valores do MAIOR para o MENOR é: ')
    print(f'{n3}, {n2}, {n1}')
'''

# Verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')