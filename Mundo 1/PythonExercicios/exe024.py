# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 'Santo'

'''
nc = str(input('Digite o nome da cidade: ')).strip()
nc = nc.title()
nc = nc.split()
print('Sua cidade começa com SANTO?')
print(f'Resposta: {"Santo" in nc}')
'''

nc = str(input('Digite o nome da cidade: ')).strip()
print('')
print(f'Sua cidade começa com SANTO?')
print(f'Resposta: {"Santo" in (nc.title().split())}')
