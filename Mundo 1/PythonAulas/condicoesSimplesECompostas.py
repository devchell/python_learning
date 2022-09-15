'''
| carro.siga()
| carro.esquerda()
| carro.siga()
| carro.direita()
| carro.siga()
| carro.direita()
| carro.siga()
| carro.esquerda()
| carro.siga()
V carro.pare()

# Possibilidades:

carro.siga()
se carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão
    carro.siga()
    carro.esquerda(0
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()


se carro.esquerda()
    bloco _V_
senão
    bloco _F_

if carro.esquerda():
    bloco True
else:
    bloco False


tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('-- FIM --')

ou

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('-- FIM --')
'''

'''
nome = str(input('Qual é seu nome? ')).strip().title()
if nome == 'João':
    print('Que nome lindo você tem!')
print(f'Bom dia, {nome}!')
'''

nome = input('Qual seu nome? ').strip().title()
print('João' in nome)
if 'João' in nome:
    print('Que nome lindo você tem!')
else:
    print('Ah, tudo bem!')
nome = nome.split()
print(f'Bom dia, {nome[0]}!')
