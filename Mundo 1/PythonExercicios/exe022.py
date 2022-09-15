# Crie um programa que leia o nome completa de uma pessoa e mostre:
# > O nome dela com todas as letras maiúsculas
# > O nome dela com todas as letras minúsculas
# > Quantas letras contém (sem considerar os espaços)
# > Quantras letras tem o primeiro nome
n = str(input('Digite seu nome: ')).strip()
print(f'Seu nome em maiúsculo é {n.upper()}')
print(f'Seu nome em minúsculo é {n.lower()}')
print(f'Seu nome possui {len("".join(n.split()))} letras')