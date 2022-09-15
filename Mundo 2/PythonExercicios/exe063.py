# Escreva um programa que leia um número (n) inteiro qualquer e mostre na tela os (n) primeiros elementos de uma
# sequência de Fibonacci.
# Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8
i = 0
j = 1
c = int(input('Quantos elementos deseja mostrar? '))
p = 3
print(i, f'> {j}', end='')
while p <= c:
    s = i + j
    print(f' > {s}', end='')
    i = j
    j = s
    p += 1