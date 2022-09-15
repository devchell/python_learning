# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tabela = ('Chapéu', 35,
          'Vestido Florido', 74.99,
          'Sapato', 95.75,
          'Meia', 9.99,
          'Anel', 130,
          'Tecido', 5,
          'Bola', 10.50,)
#x = 0
#y = 1
print('='*39)
print(f'{"LOJA 1":^39}')
print('='*39)
print('')
#for i in range(0, 5)):
#    print(f'{tabela[x]:.<30} R${tabela[y]:.2f}')
#    x += 2
#    y += 2
for i in range(0, len(tabela)):
    if i % 2 == 0:
        print(f'{tabela[i]:.<30}', end='')
    else:
        print(f'R${tabela[i]:>7.2f}')
