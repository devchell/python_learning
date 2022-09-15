# Faça um programa que leia o sexo de uma pessoa mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.
'''
con = 1
while con != 0:
    s = str(input('Digite seu sexo [F/M]: ')).strip().upper()
    print('')
    if s in 'FM':
        pass
    else:
        print('Digite um valor válido!')
        print('')
'''

s = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while s not in 'MF':
    print('SEXO INVÁLIDO!')
    s = str(input('Inform seu sexo [M/F]: ')).strip().upper()
print(f'Sexo {s} registrado com sucesso!')