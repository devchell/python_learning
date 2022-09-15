# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


# Escolha um número: [np]
# Par ou impar: [ep]
# Jogando...
# Computador escolheu PAR, você venceu!
# Computador escolheu IMPAR, você perdeu!

# np - Player number
# ep - Player choice
# i - Pair or Odd Player number
# k - Player choice
# j - Computer choice
# x - Computer random numer
# l - Pair or odd Computer number
# s - Score
from time import sleep
from random import randint
s = 0
while True:
    print('')
    np = int(input('Digite um número: '))
    ep = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    x = randint(0, 10)
    r = np + x
    print('')
    # Computer
    if r % 2 == 0:
        l = 0
    else:
        l = 1
    # Player
    if r % 2 == 0:
        i = 0
    else:
        i = 1
    if ep in 'Pp':
        k = 0 # Player pair
        j = 1 # Computer odd
    else:
        k = 1 # Player odd
        j = 0 # Computer pair

    # Game Player WON
    sleep(1)
    print('Jogando...')
    sleep(0.75)
    print('')
    if i == k == 0:
        print('Você venceu jogando par!')
        print(f'Você jogou {np} e o computador {x}, a soma é {np + x}')
        s += 1
    elif i == k == 1:
        print('Você venceu jogando ímpar!')
        print(f'Você jogou {np} e o computador {x}, a soma é {np + x}')
        s += 1

    # Game Computer WON Pair
    elif l == j == 1:
        print('Você perdeu jogando par!')
        print(f'Você jogou {np} e o computador {x}, a soma é {np + x}')
        break
    elif l == j == 0:
        print('Você perdeu jogando ímpar!')
        print(f'Você jogou {np} e o computador {x}, a soma é {np + x}')
        break
print('')
print(f'Você teve um score de {s} vitórias consecutivas!')
