'''
Adição = +
Subtração = -
Multiplicação = *
Divisão = /
Potência = **
Divisão inteira = //
Resto da divisão = %

5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2
5 % 2 == 1

Ordem de precedência:
1.()
2.**
3.*, /, //, % (por ordem de quem aparece primeiro)
4.+, -

print()
'Oi' + 'Olá' = 'OiOlá'
'Oi'*5 = 'OiOiOiOiOi'
'='*20 = '===================='
\n = Quebra de linha no mesmo código
end=' ' = Continuação da linha em códigos diferentes
'''
nome = input('Qual seu nome? ')
print(f'Prazer em te conhecer {nome:20}!')
print(f'Prazer em te conhecer {nome:>20}!')
print(f'Prazer em te conhecer {nome:<20}!')
print(f'Prazer em te conhecer {nome:^20}!')
print(f'Prazer em te conhecer {nome:=^20}!')
