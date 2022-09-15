# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:
#
# 1. Apenas os 5 primeiros colocados
# 2. Os últimos 4 colocados da tabela
# 3. Uma lsita com os times em ordem alfabética
# 4. Em que posição na tabela está o time da Corinthians
# 5. Tabela completa
from time import sleep
tabela = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Ceará SC', 'Corinthians',
          'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 'Juventude',
          'Palmeiras', 'Bragantino', 'Santos', 'São Paulo')

# Tabela completa
print(f'Tabela completa do campeonato:')
for p, i in enumerate(tabela):
    sleep(0.25)
    print(f'{p+1}. {i}')

# TOP 5
print('')
print(f'TOP 5:')
for p, i in enumerate(tabela[0:5]):
    print(f'{p+1}. {i}')
    sleep(0.25)

# Últimos 4
print('')
print('Últimos 4:')
for p, i in enumerate(tabela[-1:-5:-1]):
    print(f'{20-p}. {i}')
    sleep(0.25)

# Ordem Alfabética
print('')
print('Ordem alfabética: ')
x = 1
for i in sorted(tabela):
    print(f'{x}. {i}')
    x += 1
    sleep(0.25)

# Posição Corinthians
print('')
print('Posição do Corinthians: ')
print(f'{tabela.index("Corinthians")+1}. Corinthians')

