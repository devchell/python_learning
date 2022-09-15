'''
enquanto não maçã
    char.passo()
char.pega()

while not apple:
    char.passo()
char.pega()

while not apple:
    if chão is True:
        char.passo()
    if chão is False:
        char.pule()
    if moeda is True:
        char.pega()
char.pega()
'''


for i in range(1, 10):
    print(i)
print('FIM!')
print('')

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM!')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM!')

r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Dejesa continuar? [S/N] ')).strip().upper()

n = 1
par = impar = c = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        c += 1
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {c} números:')
print(f'{par} números pares')
print(f'{impar} números impares')
