# Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
# a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
#
# Fórmula: Peso/Altura²
from math import pow
p = float(input('Digite seu peso: '))
a = pow(float(input('Digite sua altura: ')), 2)
imc = p/a
if imc < 18.5:
    print('')
    print(f'Seu IMC é de: {imc:.1f}')
    print('Está abaixo do peso ideal')
elif imc >= 18.5 and imc < 25:
    print('')
    print(f'Seu IMC é de: {imc:.1f}')
    print('Está no peso ideal')
elif imc >= 25 and imc < 30:
    print('')
    print(f'Seu IMC é de: {imc:.1f}')
    print('Está com sobrepeso')
elif imc >= 30 and imc <= 40:
    print('')
    print(f'Seu IMC é de: {imc:.1f}')
    print('Está obeso')
elif imc >= 40:
    print('')
    print(f'Seu IMC é de: {imc:.1f}')
    print('Obesidade mórbida')