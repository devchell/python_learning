# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
c = float(input('Digite o valor da casa: R$'))
s = float(input('Digite seu salário: R$'))
t = int(input('Em quantos anos você irá pagar: '))
print('')
p = (s*(30/100))
t = t*12
pm = c/t
if pm <= p:
    print(f'As parcelas do seu empréstimo é de: R${pm:.2f} por {t} meses.')
else:
    print(f'Empréstimo negado!')

