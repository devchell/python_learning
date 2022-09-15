'''
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
senão se carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
senão
    carro.siga()
carro.pare()

#################################

carro.siga()
if carro.esquerda():
    Bloco 1
elif carro.direita():
    Bloco 2
elif carro.ré():
    Bloco 3
else:
    Bloco 4
carro.pare()

n = str(input('Qual seu nome? ')).strip().title()
if n == 'João':
    print('Que nome bonito!')
elif n == 'Pedro' or n == 'Ana' or n == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif n in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome fêmea')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {n}!')
'''

for c in range(0, 5):
    print(c)