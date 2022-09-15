# Crie um programa que elaia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
# (Desconsiderando o flag)
i = c = s = 0
while True:
    i = int(input('Digite um valor: '))
    if i == 999:
        break
    c += 1
    s += i
print(f'Você digitou {c} números e a soma deles é {s}')
