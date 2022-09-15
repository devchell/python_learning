# Crie um progrma que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
n = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze'
     , 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
     i = int(input('Qual número deseja ler por extenso (1 - 20): '))
     if 0 <= i <= 20:
          break
     print('Valor não existente, tente novamente!')
     print('')
c = n[i-1]
print('')
print(c)