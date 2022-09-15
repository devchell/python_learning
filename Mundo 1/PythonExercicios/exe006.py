# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.
n = input('Digite um número: ')
d = float(n)*2
t = float(n)*3
rq = float(n)**(1/2)
print(f'Seu número ({n}) tem como: \nDobro: {d}\nTriplo: {t}\nRaiz quadrada: {rq:.2f}')
