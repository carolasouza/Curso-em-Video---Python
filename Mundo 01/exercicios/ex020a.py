import random

print('===== DESAFIO 20 =====')
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
alunos = input('Digite o nome dos 4 alunos separados um espaço: ')
alunos_list = alunos.split()

for i in range(4):
    alunos_list[i] = str(alunos_list[i])

print('\nAlunos incluídos na lista: {}'.format(alunos_list))
random.shuffle(alunos_list)
print('Ordem de apresentação:\n{}'.format(alunos_list))
