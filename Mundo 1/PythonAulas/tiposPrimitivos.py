'''
# int = números inteiro (7, -4, 0, 9875)
# float = números reais (4.5, 0.076, -15.223, 7.0)
# bool = True ou False
# str = palavra ('Olá', '', '8.5', '64')
'''

n1 = input('Digite um número: ')
n2 = input('Digite mais um número: ')
s = int(n1) + int(n2)
print(f'A soma vale {s}')
print(type(s))

print('')

n1 = input('Digite um número: ')
n2 = input('Digite mais um número: ')
s = float(n1) + float(n2)
print(f'A seoma vale {s}')
print(type(s))

print('')

n1 = input('Digite um valor: ')
print(bool(n1))

print('')

n1 = input('Digite algo: ')
n2 = input('Digite mais algo: ')
print(f'Você digitou primeiro: {n1}')
print(type(n1))
print(f'Logo após, digitou: {n2}')
print(type(n2))

'''
n = input('Digite algo: ')
isn = n.isalnum()
isa = n.isalpha()
isd = n.isdigit()
isan = n.isalnum()
isu = n.isupper()
isl = n.islower()
'''