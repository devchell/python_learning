# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
n = str(input('Digite seu nome: ')).strip()
n = n.title()
print(f'Há SILVA em seu nome?')
print(f'Resposta: {"Silva" in n}')
