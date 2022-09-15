# lanche = (Tupla) [Lista] {Dicionário}
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Maçã', 'Jaca', 'Strogonoff')
print(lanche)
print('''
''')

# Forma 1
print('Forma 1:')
for p, c in enumerate(lanche):
    # P = Posição
    # C = Comida
    print(f'{c} (na posição {p})')
print('''
''')

# Forma 2
print('Forma 2:')
for c in range(0, len(lanche)):
    # C = Comida
    print(f'{lanche[c]} (na posição {c})')
print('''
''')

# Forma 3
print('Forma 3:')
i = 0
for c in lanche:
    print(f'{c} (na posição {i})')
    i += 1
print('''
''')

# Forma 4
i = 0
print('Forma 4:')
for c in lanche:
    print(f'{c}')
print('''
''')

# Junção
a = (1, 3, 5)
b = (2, 4, 6, 8)
c = a + b
print(c)
# Ou
print(a + b)
print(c.count(5)) # Contagem do valor no ()
print(c.index(5)) # Qual primeira aparição


