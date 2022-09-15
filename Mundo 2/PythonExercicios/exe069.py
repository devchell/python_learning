# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final mostre:
# 1. Quantas pessoas tem mais de 18 anos.
# 2. Quantos homens foram cadastrados.
# 3. Quantas mulheres com menos de 20 anos.
agec = sexmc = safc = i = 0
sex = ' '
while True:
    name = str(input('Digite seu nome: ')).strip().title()
    age = int(input('Digite sua idade: '))
    while sex not in 'MF':
        sex = str(input('Digite seu sexo [F/M]: ')).strip().upper()
    if age > 18:
        agec += 1
    if sex in 'Mm':
        sexmc += 1
    if sex in 'Ff':
        if age < 20:
            safc += 1
    print('')
    while i != 1 and i != 2:
        i = int(input('''Deseja continuar? 
1. Sim
2. Não
R: '''))
    print('')
    if i == 2:
        break
print(f'''Neste local há:
- {agec} pessoa(s) com mais de 18 anos.
- {sexmc} homen(s) cadastrado(s).
- {safc} mulher(es) com menos de 20 anos.''')
print('')
print('Obrigado, por usar nosso programa!')
