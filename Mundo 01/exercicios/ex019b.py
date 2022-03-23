import random
print('===== DESAFIO 19 =====')
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

print('\nDigite o nome dos (as) 4 alunos (as) abaixo.')
alunos = []*3
alunos.append(str(input('Primeiro: ')))
alunos.append(str(input('Segundo: ')))
alunos.append(str(input('Terceiro: ')))
alunos.append(str(input('Quarto: ')))
print('\nAlunos incluídos: {}'.format(alunos))
print('Aluno(a) selecionado(a): {}'.format(random.choice(alunos)))
