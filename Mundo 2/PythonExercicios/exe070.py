# Crie um programa que leia um nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# 1. Qual é o total gasto na compra.
# 2. Quantos produtos custam mais de R$1.000,00
# 3. Qual é o nome do produto mais barato
pp1k = tp = lowp = x = 0
plow = ''
print(f'{" Caixa ":=^70}')
print('')
while True:
    pn = str(input('Nome do produto: ')).strip().title()
    print('')
    pp = float(input('Preço do produto: R$'))
    print('')
    x += 1

    # +1k
    if pp > 1000:
        pp1k += 1

    # Low price
    if x == 1:
        lowp = pp
        plow = pn
    else:
        if pp < lowp:
            lowp = pp
            plow = pn
    i = int(input('''Deseja continuar?
1. Sim
2. Não
R: '''))
    print('')
    tp += pp
    if i == 2:
        break
print(f'''Gasto total: R${tp:.2f}
Há {pp1k} produtos com mais de R$1000,00
O produto mais barato é {plow} custando R${lowp:.2f}''')
