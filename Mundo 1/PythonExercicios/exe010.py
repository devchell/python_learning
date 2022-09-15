# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27
din = float(input('Quantos reais você tem? R$'))
dolar = din/3.27
print(f'Você tem R${din:.2f} e poderá comprar US${dolar:.2f}')