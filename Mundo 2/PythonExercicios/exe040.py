# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrandouma mensagem no final, de acordo com a
# média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
m1 = float(input('Digite a nota da primeira prova: '))
m2 = float(input('Digite a nota da segunda prova: '))
m = (m1+m2)/2
if m < 5:
    print('')
    print(f'Sua média foi de: {m:.1f}')
    print('REPROVADO!')
elif m >= 5 and m < 7: # elif 7 > m >= 5:
    print('')
    print(f'Sua média foi de: {m:.1f}')
    print(f'RECUPERAÇÃO')
elif m >= 7:
    print('')
    print(f'Sua média foi de: {m:.1f}')
    print('APROVADO!')