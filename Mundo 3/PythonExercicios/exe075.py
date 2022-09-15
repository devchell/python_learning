# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# 1. Quantas vezes apareceu o valor 9
# 2. Em que posição foi digitado o primeiro valor 3
# 3. Quais foram números pares
num = (int(input('Digite o 1º valor: ')),
     int(input('Digite o 2º valor: ')),
     int(input('Digite o 3º valor: ')),
     int(input('Digite o 4º valor: ')))
print(''
      )
# Quantidade de 9
i = num.count(9)
print(f'1. O número 9 apareceu {i} vezes.')
print('')

# Posição primeiro 3
if 3 in num:
    i = num.index(3)
    print(f'2. O número 3 teve sua primeira aparição na posição: {i+1}')
    print('')
else:
    print('2. Nenhum número 3 foi digitado.')
    print('')

# Números pares
print('3. Os números pares são: ', end='')
for k in num:
    if k % 2 == 0:
        print(k, end=' ')