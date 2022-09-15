# Refaça o 'exe051.py', lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura WHILE.
i = 1
print(f'{" PA CALCULATOR ":=^60}')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
while i <= 10:
    print(f'{p}', end='')
    print(' → 'if i < 10 else '', end='')
    p += r
    i += 1
