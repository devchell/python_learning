# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa
# progressão.
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
print(d)
print(d + r)
for c in range(p, d + r, r): # Nunca contará o ultimo número, por isso d + r = 30 e o d = 27, porém o python irá contar
                             # até o 29, por isso é importante somar r com d.
    print(f'{c}', end=' > ')
print('Acabou')