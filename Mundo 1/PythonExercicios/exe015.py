# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.
km = float(input('Quantos KM foram percorrídos? '))
dias = int(input('Quantos dias de uso? '))
preco = (dias*60)+(km*0.15)
print(f'Você usou o carro por {dias} dias e rodou {km}KM, resultando um valor de R${preco:.2f}')