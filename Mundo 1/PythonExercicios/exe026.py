# Faça um programa que leia uma frase e mostre:
# > Quantas vezes aparece a letra A
# > Em que posição ela aparece a primeira vez
# > Em que posição ela aparece a última vez

'''
f = str(input('Digite uma frase: ')).strip()
f = f.upper()
print('')
print(f'Quantas vezes aparece a letra A?')
print(f'Resposta: {f.count("A")}')
print('')
print(f'Qual a posição da primeira aparição da letra A?')
print(f'Resposta: {f.find("A")}')
print('')
print(f'Qual a posição da última aparição da letra A?')
print(f'')
'''

f = str(input('Digite uma frase: ')).upper().strip()
print('')
print(f'Quantas vezes aparece a letra A?')
print(f'Resposta: {f.count("A")}')
print('')
print(f'Qual a posição da primeira aparição da letra A?')
print(f'Resposta: {f.find("A")+1}')
print('')
print(f'Qual a posição da última aparição da letra A?')
print(f'Reposta: {f.rfind("A")+1}') # Pode usar R ou L em qualquer função para procurar da direta ou da esquerda (rfind)
print(f'')
