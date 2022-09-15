# Refaça o 'exe009.py', mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número: '))
m = int(input('Digite quantas vezes quer multiplicar: '))
c = 1
print('')
for i in range(1, m+1):
    print(f'{n}x{c}={n*c}')
    c += 1
print('')
print(f'Tabuada finalizada!')