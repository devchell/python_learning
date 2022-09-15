# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Digite o valor do salário: R$'))
aum = sal+(sal*(15/100))
print(f'O salário do funcionário vai de R${sal:.2f} para R${aum:.2f} (+15%)')