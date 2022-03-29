print('===== DESAFIO 22 =====')
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print('\nAnalisando seu nome:')
print('1. Apenas com letras maiúsculas: {}'.format(nome.upper()))
print('2. Apenas com letras minúsculas: {}'.format(nome.lower()))
# print('3. Seu nome completo contém {} letras'.format(len(nome) - nome.count(' ')))

nomes = nome.split()
print('3. Seu nome completo contém {} letras'.format(len(''.join(nomes))))
print('4. Seu primeiro nome é {} e esta palavra tem {} letras'.format(nomes[0], len(nomes[0])))
# print('4. Seu primeiro nome é {} e esta palavra tem {} letras'.format(nomes[0], nome.strip().find(' ')))
