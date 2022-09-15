# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
f = str(input('Digite uma frase: ')).strip().upper().split()
j = ''.join(f)
inv = ''
for i in range(len(j) - 1, -1, -1):
    inv += j[i]
if j == inv:
    print(f'A frase é um palíndromo!')
    print(f'Frase: {j} {inv}')
else:
    print('A frase não é um palíndromo!')
    print(f'Frase: {j} {inv}')