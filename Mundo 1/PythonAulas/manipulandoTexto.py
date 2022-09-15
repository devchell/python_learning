'''
frase = 'Curso em Vídeo Python'
    # 0 - 20 caracteres (21 caracteres)

# 1. Fatiamento #

print(frase[9]) #-> V

print(frase[9:13]) #-> Víde
    # Número do caractere -1

print(frase[9:21]) #-> Vídeo Python
    # Vai até o ultimo caractere (21 - 1 = 20)

print(frase[9:21:2]) #-> VdiPto
    # Vai do caractere 9 até 21, pulando de 2 em 2

print(frase[:5]) #-> Curso
    # Do início até o caractere -1 (4)

print(frase[15:]) #-> Python
    # Vai do caractere 15 até o ultimo

print(frase[9::3]) #->VePh
    # Vai do caractere 9 até o final da string, pulando de 3 em 3


# 2. Funções #

print(len(frase)) #-> 21
    # Mostra o comprimento da frase (Quantidade de caracteres)

print(frase.count('o')) #-> 3
    # Conta todos os 'o' (minúsculos) na string

print(frase.count('o', 0, 13)) #-> 1
    # Conta todos os 'o' (minúsculos) do caractere 0 ao caractere 13 - 1 (12)

print(frase.find('deo')) #-> 11
    # Mostra em qual caractere inicia a string buscada

print(frase.find('Android')) #-> -1
    # Retorna o valor sem resultado na string

print('Curso' in frase) #-> True
    # Retorna um valor booleano caso haja a palavra na string


# 3. Transformação #

print(frase.replace('Python', 'Android')) #-> Curso em vídeo Android
    # Procura o primeiro elemento e substitui pelo segundo (de forma secundária)

print(frase.upper()) #-> CURSO EM VÍDEO PYTHON
    # Altera todas os caracteres em minúsculo para maiúsculo

print(frase.lower()) #-> curso em vídeo python
    # Altera todas os caracteres em maiúsculo em minúsculo

print(frase.capitalize()) #-> Curso em vídeo python
    # Coloca todas os caracteres em minúsculo, menos o primeiro carectere que transformará/deixará em maiúscula

print(frase.title()) #-> Curso Em Vídeo Python
    # O primeiro caractere de cada palavra será colocada em maiúscula e o resto em minúscula

frase = '   Aprenda Python  '

print(frase.strip()) #-> 'Aprenda Python'
    # Remove os espaços excedentes (esquerda e direita)

print(frase.rstrip()) #-> '   Aprenda Python'
    # Remove os espaços excedentes (apenas da direita)

print(frase.lstrip()) #-> 'Aprenda Python  '
    #Remove os espaços excedentes (apenas da esquerda)

frase = 'Curso em vídeo Python'


# 3. Divisão #

print(frase.split()) #-> ['Curso', 'em', 'vídeo', 'Python']
    # Divide a string em uma lista, recebendo uma indexação nova, sendo enumerada uma por uma respectivamente com seus
    # caracteres
    # [0, 1, 2, 3] = contagem de palavras
    # 0 = [0, 1, 2, 3, 4] contagem de caracteres na palavra 0
    # 1 = [0, 1] contagem de caracteres na palavra 1
    # 2 = [0, 1, 2, 3, 4] contagem de caracteres na palavra 2
    # 3 = [0, 1, 2, 3, 4, 5] contagem de caracteres na palavra 3

frase = frase.split()

# 4. Junção #

print('-'.join(frase)) #-> Curso-em-Vídeo-Python
    # Junta a string (dividida) com '-'

print(' '.join(frase)) #-> Curso em Vídeo Python
    # Junta a string (dividida) com ' '
'''

# Prática

frase = 'Curso em Vídeo Python'
print(frase[1:15])

print(frase[1:15:2])

print(frase[1::2])

print(frase[::2])

print(frase.count('o'))

print(frase.count('O'))

print(frase.upper().count('O'))

print(len(frase))

frase = '   Curso em Vídeo Python   '

print(len(frase))

print(len(frase.strip()))

frase = 'Curso em Vídeo Python'

print(frase.replace('Python', 'Android'))

print('Curso' in frase)

print(frase.find('Curso'))

print(frase.find('curso'))

print(frase.lower().find('vídeo'))

print(frase.split())

div = frase.split()
print(div[0])
print(div[1])
print(div[2])
print(div[3])

print(div[2][3])

frase = frase.split()
frase = ''.join(frase)
print(len(frase))

print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore 
magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''')
