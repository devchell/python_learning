# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.
metros = input('Digite um número: ')
cen = float(metros)*100
mm = float(metros)*1000
print(f'O número no qual foi digitado tem como valor: \nMetros: {metros}m\nCentimetros: {cen:.0f}cm\nMilímetros: {mm:.0f}mm')