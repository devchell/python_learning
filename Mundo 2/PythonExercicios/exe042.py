# Refaça o 'exe035.py' dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if a < b + c and b < a + c and c < a + b:
    print('')
    print('Podem formar um triângulo!')
    print('')
    print('Tipo:')
    '''
    if a == b and c == a and b == c:
        print('')
        print('É um triângulo EQUILÁTERO')
    elif a == b and c != b and c != a or b == c and a != b and a != c or a == c and b != c and b != a:
        print('')
        print('É um triâgulo ISÓSCELES')
    elif a != b and b != c and c != a:
        print('')
        print('É um triângulo ESCALENO')
    '''
    if a == b == c:
        print('É um triângulo EQUILÁTERO')
    elif a != b != c != a:
        print('É um triângulo ESCALENO')
    else:
        print('É um triângulo ISÓSCELES')
else:
    print('')
    print('Você não poderá criar um triângulo com esses valores')