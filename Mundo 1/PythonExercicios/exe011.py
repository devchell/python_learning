# Faça um programa que leia a largura e a altura de uma parede em mestros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
lar = float(input('Largura da parede (Em metros): '))
alt = float(input('Altura da parede (Em metros): '))
area = lar*alt
tin = area/2
print(f'Sua parede tem {lar:.1f}x{alt:.1f} tendo sua área de {area:.2f}m², então você irá precisar de {tin:.1f}L de tinta')
