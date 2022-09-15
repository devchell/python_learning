capital = float(input('Digite o valor mensal: '))
meses_aplicados = int(input('Quantos meses o valor será aplicado: '))
juros_mensal = (11.75)/12
mes = 1
capital_mensal = 0

for i in range(1, meses_aplicados + 1):
    lucro_mensal = (capital*juros_mensal)
    lucro_mensal_total = capital+juros_mensal
    capital_mensal = capital+lucro_mensal_total
    print(f'O lucro no mês {mes}, foi de R${lucro_mensal_total:.2f}')
    mes += 1