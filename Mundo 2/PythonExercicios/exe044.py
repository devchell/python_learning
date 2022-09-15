# Desenvolva um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
v = float(input('Digite o valor do produto: R$'))
print('')
print('''Selecione a opção de pagamento:
1. À Vista (Dinheiro/Cheque)
2. À Vista (Cartão)
3. Até 2x (Cartão)
4. 3x ou mais (Cartão)''')
print('')
i = int(input('Digite a opção: '))
if i == 1:
    j = v-(v*10/100)
    print('')
    print(f'Método de pagamento escolhido: ')
    print('À Vista (Dinheiro/Cheque)')
    print('')
    print(f'Total: R${j:.2f}')
elif i == 2:
    j = v-(v*5/100)
    print('')
    print(f'Método de pagamento escolhido: ')
    print('À Vista (Cartão)')
    print('')
    print(f'Total: R${j:.2f}')
elif i == 3:
    print('')
    print(f'Método de pagamento escolhido: ')
    print('Até 2x (Cartão)')
    print('')
    print(f'Total: R${v:.2f}')
    print(f'Parcelas: 1 x R${v:.2f}')
    print(f'          2 x R${v/2:.2f}')
elif i == 4:
    j = v+(v*20/100)
    print('')
    print(f'Método de pagamento escolhido: ')
    print('3x ou mais (Cartão)')
    print('')
    print(f'Total: R${j:.2f}')
    print(f'Parcelas: 3 x R${j/3:.2f}')
    print(f'          4 x R${j/4:.2f}')
    print(f'          5 x R${j/5:.2f}')
    print(f'          6 x R${j/6:.2f}')