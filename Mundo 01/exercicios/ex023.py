print('===== DESAFIO 23 =====')
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
# tentar como string e matematicamente

num = int(input('\nDigite um inteiro entre 0 e 9999: '))

print('Milhar: {}'.format(num // 1000 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Dezena: {}'.format(num // 10 % 10))
print('Unidade: {}'.format(num // 1 % 10))
