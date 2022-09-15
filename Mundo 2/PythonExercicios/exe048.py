# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
n = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        n += i
print(n)
print('')