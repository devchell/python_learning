# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o valor do produto: R$'))
desc = p-(p*(5/100))
print(f'O valor do produto é R${p:.2f}, com desconto o valor vai para R${desc:.2f} (-5%)')