# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
n = 1
for i in range(1, 51):
    if n%2==0:
        print(n)
    else:
        pass
    n += 1
print('')
print('Apenas os valores pares')
'''

for i in range (2, 51, 2):
    print(i)
print('Números pares!')