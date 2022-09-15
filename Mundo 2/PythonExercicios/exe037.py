# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1. Binário
# 2. Octal
# 3. Hexadecimal
n = int(input('Digite um número: '))
print('')
print('''Escolha uma das opções:
[1] Binário
[2] Octal
[3] Hexadecimal''')
print('')
i = int(input('Digite a opção selecionada: '))

if i == 1:
    print('')
    print(f'Seu número Binário é: {bin(n)}')
elif i == 2:
    print('')
    print(f'Seu número em Octal é: {oct(n)}')
else:
    print('')
    print(f'Seu número em Hexadecimal é: {hex(n)}')
