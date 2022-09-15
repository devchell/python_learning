# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome escolhido.
from random import choice
alunos = ['Amanda', 'Ana', 'Matheus', 'Carlos']
print(f'O aluno escolhido foi {choice(alunos)}')