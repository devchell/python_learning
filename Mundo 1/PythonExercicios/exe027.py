# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

'''
n = str(input(('Digite seu nome: '))).strip().title().split()
print('')
print('Seu primeiro nome é:')
print(f'Respota: {n[0]}')
print('')
print('Seu ultimo nome é: ')
print(f'')
'''

n = str(input(('Digite seu nome: '))).strip().title().split()
print('')
print('Seu primeiro nome é:')
print(f'Respota: {n[0]}')
print('')
print('Seu ultimo nome é: ')
print(f'Respota: {n[len(n)-1]}')
    # Len mostra quantos Split há (começando do 1)
    # Já o Python começa do 0, então Len = 5 // Python = 4 (len(n)-1) => 5 - 1 = 4