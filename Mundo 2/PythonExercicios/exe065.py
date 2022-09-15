# Crie um programa que leia vários números inteiro pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele uer ou não continuar
# a digitar mais valores
i = 'S'
m = q = s = ma = me = 0
while i in 'S':
    n = int(input('Digite um valor: '))
    s += n
    q += 1
    if q == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    i = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('')
m = s/q
print(f'Você digitou {q} números, sendo sua soma: {s} com média de: {m}')
print(f'Sendo eles {ma} o maior número e {me} o menor número.')
