# lanche = (Tupla) [Lista] {Dicionário}
lanche = ['Hambúguer', 'Suco', 'Pizza', 'Pudim']
print(lanche) # Lista original

lanche[3] = 'Picolé' # Lista é mutável, já tupla não!
print(lanche) # Lista mutada

lanche.append('Cookie') # Adiciona um item extra
print(lanche)

lanche.insert(0, 'Hotdog') # Adiciona um item extra em uma posição expecífica
print(lanche)

# Método de remoção de item em uma lista

del lanche[3] # Indica o indice
print(lanche)

lanche.pop() # Normalmente usado para remover o último, porém pode ser indicado o índice
print(lanche)

lanche.remove('Hotdog') # Remove o valor dentro da lista
print(lanche)
########################################################################################################################
num = [2, 5, 9, 1]
print(num)
print(f'Essa lista tem {len(num)} elementos')
num[2] = 3
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.append(7)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.sort()
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.insert(2, 0)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.pop()
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')
if 4 in num:
    num.remove(4)
else:
    print(f'{num} (Não há nenhum número para se remover)')
########################################################################################################################
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(f'{v}', end = ' ')
print('')
valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

