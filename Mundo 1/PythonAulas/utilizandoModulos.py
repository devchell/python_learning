'''
import {módulo} = importa todos as funções do módulo
from {módulo} import {funç} = importa apenas a função mencionada no import do módulo
from {módulo} import {funç1}, {funç2}, {funç3} = você pode importar quantas funções quiser, não só uma por linha


Módulo de matemática:

Nome do módulo: math
Nome dos itens (principais): ceil, floor, trunc, pow, sqrt, factorial

import math = (importará todas as funções)
from math import ceil = (importará apenas a função ceil)
from math import floor, trunc, pow = (importará apenas as funções floor, trunc e pow)
'''

import math
num = int(input('Digite um número: '))
print(f'A raiz quadrada de {num} é {math.ceil(math.sqrt(num))}')

from math import floor, sqrt
num = int(input('Digite um número: '))
print(f'A raiz quadrada de {num} é {floor(sqrt(num))}')

#Biblioteca de emoji

import emoji
print(emoji.emojize("Olá mundo :earth_americas:", use_aliases=True))