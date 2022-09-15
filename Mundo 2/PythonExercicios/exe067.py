# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
from time import sleep
n = 0
x = 1
while True:
    print('')
    n = int(input('Digite um valor: '))
    print('')
    while x <= 10:
        sleep(0.5)
        print(f'{n} x {x} = {n * x}')
        x += 1
    print('')
    c = str(input('Deseja continuar? [S/N] ')).upper().strip()
    print('')
    if c in 'Ss':
        n = 0
        x = 1
    elif c in 'Nn':
        break
print('Muito obrigado por usar nossa calculadora!')