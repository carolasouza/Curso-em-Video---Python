from random import shuffle

print('===== DESAFIO 20 =====')
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
print('\nDigite o nome dos (as) 4 alunos (as) abaixo:')
alunos = []*3
alunos.append(str(input('Primeiro: ')))
alunos.append(str(input('Segundo: ')))
alunos.append(str(input('Terceiro: ')))
alunos.append(str(input('Quarto: ')))
print('\nAlunos incluídos: {}'.format(alunos))
shuffle(alunos)
print('Ordem de apresentação: {}'.format(alunos))
