# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
m = 0
maior = 0
nmaior = ''
for i in range(1, 5):
    # Informações
    n = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    s = str(input('Sexo [F/M]: ')).strip()
    print('')

    # Média de idade
    m1 = idade/4
    m += m1

    # Sexo e mais velho
    if s in 'Mm':
        if i == 1:
            maior = idade
        else:
            if idade > maior:
                nmaior = n
                maior = idade
            else:
                pass
    else:
        pass

print(f'A média de idade do grupo é: {m}.')
print(f'O homem mais velho é {nmaior} e tem {maior} anos.')
