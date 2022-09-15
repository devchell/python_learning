# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por
# cada KM para viagens de até 200Km e R$0.45 para viagens mais longas.
dis = float(input('Qual a distância da viagem? '))
print('')
if dis <= 200:
    print(f'Sua viagem é curta, então custará {dis*0.5}')
else:
    print(f'Sua viagem é longa, então custará {dis*0.45}')