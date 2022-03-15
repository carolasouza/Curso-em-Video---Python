print('===== DESAFIO 13 =====')
print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')

sal = float(input('\nDigite o salário: '))
aumento = 15/100
print('\nO salário com aumento será de: R${:.2f}'.format(sal * (1 + aumento)))
