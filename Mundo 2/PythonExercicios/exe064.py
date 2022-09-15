# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).
s = q = 0
i = int(input('Digite um valor: '))
while i != 999:
    q += 1
    s += i
    i = int(input('Digite um valor: '))
print('')
print(f'Você digitou {q} números!')
print(f'A soma entre ele é {s}')