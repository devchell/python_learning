# Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
v = int(input('Digite um valor: R$'))
i = 50 # céd
k = 0 # totcéd

while True:
    if v >= i:
        v -= i
        k += 1
    else:
        if k > 0:
            print(f'Você pode sacar {k} cédulas de R${i}')
        if i == 50:
            i = 20
        elif i == 20:
            i = 10
        elif i == 10:
            i = 1
        k = 0
        if v == 0:
            break
