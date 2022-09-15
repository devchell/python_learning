# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
print('Digite sua data de nascimento:')
d = int(input('Dia: '))
m = int(input('Mês: '))
a = int(input('Ano: '))
print('')
print(f'Data de nascimento: {d}/{m}/{a}')
print('')
aa = date.today().year
i = aa-a
if i == 18:
    print('Você terá que se alistar neste ano!')
elif i < 18:
    print(f'Você terá que se alistar em {18-i} ano(s)')
elif i > 18:
    print(f'Já passou {i-18} anos do seu alistamento')

# Melhorar o programa