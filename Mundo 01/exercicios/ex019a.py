import random
print('===== DESAFIO 19 =====')
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
alunos = input('\nDigite o nome dos 4 alunos separados por um espaço: ')
alunos_list = alunos.split()

for i in range(4):
    alunos_list[i] = str(alunos_list[i])

# print('\nAlunos incluídos na lista: {}'.format(alunos_list))
print('Aluno selecionado: {}'.format(random.choice(alunos_list)))
