from math import trunc
print('===== DESAFIO 16 =====')

# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Exemplo:
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6. (math)

num = float(input('\nDigite um número: '))
print('\nO número {} tem a parte inteira {}.'.format(num, int(num)))
print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))
