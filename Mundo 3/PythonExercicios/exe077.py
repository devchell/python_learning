# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cadapalavra, quais são as suas vogais.
w = ('Analfabeto', 'Circulo', 'Macaco', 'Computador', 'Mesa', 'Cadeira', 'Amortecedor')

for p in w:
    print(f'\n{p} tem as vogais: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')
    print('')