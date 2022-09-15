# A confederação nacional de natação precisa de um programa que leia o ano de anscimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER
i = int(input('Digite sua idade: '))
if i <= 9:
    print('')
    print('Você pertence à categoria MIRIM')
elif i <= 14:
    print('')
    print('Você pertence à categoria INFANTIL')
elif i <= 19:
    print('')
    print('Você pertence à categoria JUNIOR')
elif i <= 25:
    print('')
    print('Você pertence à categoria SÊNIOR')
elif i > 25:
    print('')
    print('Você pertence à categoria MASTER')