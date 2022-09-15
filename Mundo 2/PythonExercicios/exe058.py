# Melhore o jogo do 'exe028.py' onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai
# tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
# from random import choice
# n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# epc = choice(n)
epc = randint(0, 10)
epl = int(input('Digite um valor: '))
t = 1
while epl != epc:
    print(f'Você errou, o computador escolheu {epc}, tente novamente!')
    epl = int(input('Digite um valor: '))
    # epc = choice(n)
    epc = randint(0, 10)
    t += 1
print('Parabéns, você acertou!')
print(f'Foi preciso {t} tentativas para acertar.')