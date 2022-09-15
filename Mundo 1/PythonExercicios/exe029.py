# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada KM acima do limite.
v = float(input('Digite a velocidade do carro (Km/h): '))
print('')
if v > 80:
    print('VOCÊ FOI MULTADO!')
    print('')
    print(f'Você pagará R${(v-80)*7:.2f} por ultrapassar {v-80}Km/h acima do permitido!')
else:
    print('Você passou pelo radar, obrigado por andar com segurança!')