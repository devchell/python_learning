# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250.00, calcule um aumento de 10%.
# Para salário inferiores ou iguais, o aumente é de 15%.
s = float(input('Digite seu salário: R$'))
if s > 1250:
    a = (10/100)
    print('')
    print(f'Seu novo salário com {a*100:.0f}% de aumento será de: R${a*s+s} (+{a*s})')
else:
    a = (15/100)
    print('')
    print(f'Seu novo salário com {a*100:.0f}% de aumento será de: R${a*s+s} (+{a*s})')