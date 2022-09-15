# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
i = 0
while i != 5:
    print('')
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    print('')
    print('Escolha: ')
    print('''
1. Somar
2. Multiplicar
3. Maior
4. Novos números
5. Sair do programa''')
    print('')
    i = int(input('Selecione uma opção: '))
    if i == 1:
        r = n1 + n2
        print(f'A soma dos valores {n1} e {n2} é {r}')
        print('')
        i = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if i == 'N':
            i = 5
        else:
            i = 0
    elif i == 2:
        r = n1 * n2
        print(f'A multiplicação dos valores {n1} e {n2} é {r}')
        print('')
        i = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if i == 'N':
            i = 5
        else:
            i = 0
    elif i == 3:
        maior = menor = 0
        if n1 > n2:
            maior = n1
            menor = n2
        elif n2 > n1:
            maior = n2
            menor = n1
        print(f'O maior valor é {maior}')
        print(f'O menor valor é {menor}')
        print('')
        i = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if i == 'N':
            i = 5
        else:
            i = 0
    elif i == 4:
        print('')
        print('Digite novamente!')
        print('')
        pass
    elif i == 5:
        i = 5
    else:
        print('')
        print('Não entendi, vamos tentar novamente!')
        print('')
print('')
print('Obrigado por usar nosso programa!')