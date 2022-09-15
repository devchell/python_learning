# Desenvolva um programa que leia seis números inteiros e mostre a soma daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-os.
v = 0
for i in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        v += n
    else:
        pass
print(f'A soma de todos os valores pares é: {v}')
