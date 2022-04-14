print('===== DESAFIO 27 =====')
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza
# primeiro: Ana
# último: Souza

nome = input('Escreva seu nome completo: ').strip()
nomes = nome.split()
print('Primeiro nome: {}'.format(nomes[0]))
print('Último nome: {}'.format(nomes[-1]))
print('Último nome: {}'.format(nomes[len(nomes)-1]))
