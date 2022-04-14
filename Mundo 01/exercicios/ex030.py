print('===== DESAFIO 30 =====')
# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

print('-'*30)
print('Este número é PAR ou ÍMPAR?')
print('-'*30)

num = int(input('\nDigite um número: '))
if (num % 2) == 0:
    print('\nEste número é PAR.')
else:
    print('\nEste número é ÍMPAR.')
