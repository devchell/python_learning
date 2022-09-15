# Melhore o 'exe061.py', perguntando se o usuário quer mostrar mais alguns termos. O programa encerra quando ele disser
# que quer motrar 0 termos.
i = 0
dt = 0
print(f'{" PA CALCULATOR ":=^60}')
while i != 3:
    print('')
    print('''Selecione uma opção: 
1. Calcular os 10 primeiros termos
2. Inserir quantidade de termos
3. Sair''')
    i = int(input('Opção: '))
    print('')
    if i == 1:
        p = int(input('Digite o primeiro termo: '))
        r = int(input('Digite a razão: '))
        d = p + (10 - 1) * r
        for c in range(p, d + r, r):
            print(c, end='')
            print(' → ' if c != d else '', end='')
        print('\n')
        j = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if j == 'S':
            i = 0
        elif j == 'N':
            i = 3
    if i == 2:
        p = int(input('Digite o primeiro termo: '))
        r = int(input('Digite a razão: '))
        dt = int(input('Digite a quantidade de termos: '))
        d = p + (dt - 1) * r
        for c in range(p, d + r, r):
            print(c, end='')
            print(' → ' if c != d else '', end='')
        print('\n')
        j = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if j == 'S':
            i = 0
        elif j == 'N':
            i = 3
    if i == 3:
        pass
    else:
        print('Não entendi, vamos tentar novamente?')
        i = 0
print('')
print('Programa finalizado com sucesso!')