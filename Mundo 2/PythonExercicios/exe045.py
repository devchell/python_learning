# Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
from time import sleep
pd = 'Pedra'
pp = 'Papel'
ts = 'Tesoura'
jokenpo = [pd, pp, ts]
ec = choice(jokenpo)
print('''Faça sua jogada:

[1] Pedra
[2] Papel
[3] Tesoura
''')
sleep(1)
i = int(input('Digite sua escolha: '))
if i == 1:
    i = 'Pedra'
elif i == 2:
    i = 'Papel'
elif i == 3:
    i = 'Tesoura'
print('')
sleep(0.75)
print('Jo')
sleep(0.75)
print('Ken')
sleep(1)
print('PO!')
sleep(0.7)

# Empates
if ec == i:
    print('')
    print('EMPATE!')
    print('')
    print('Opção escolhida:')
    print(f'Jogador: {i}')
    print(f'Computador: {ec}')

# Vencedor Ganhando
elif ec == ts and i == 'Pedra':
    print('')
    print('VITÓRIA!')
    print('')
    print('Opção escolhida:')
    print(f'Jogador: {i}')
    print(f'Computador: {ec}')
elif ec == pd and i == 'Papel':
    print('')
    print('VITÓRIA!')
    print('')
    print('Opção escolhida:')
    print(f'Jogador: {i}')
    print(f'Computador: {ec}')
elif ec == pp and i == 'Tesoura':
    print('')
    print('VITÓRIA!')
    print('')
    print('Opção escolhida:')
    print(f'Jogador: {i}')
    print(f'Computador: {ec}')

# Computador Ganhando
elif ec == pd and i == 'Tesoura':
    print('')
    print('DERROTA!')
    print('')
    print('Opção escolhida:')
    print(f'Jogador: {i}')
    print(f'Computador: {ec}')
if ec == pp and i == 'Pedra':
    print('')
    print('DERROTA!')
    print('')
    print('Opção escolhida:')
    print(f'Jogador: {i}')
    print(f'Computador: {ec}')
if ec == ts and i == 'Papel':
    print('')
    print('DERROTA!')
    print('')
    print('Opção escolhida:')
    print(f'Jogador: {i}')
    print(f'Computador: {ec}')

# Fazer IF dentro de IF
