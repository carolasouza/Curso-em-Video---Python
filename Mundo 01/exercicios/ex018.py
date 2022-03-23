from math import sin, cos, tan, radians
print('===== DESAFIO 18 =====')
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

angulo = float(input('\nDigite o ângulo em graus: '))
print('\nÂngulo: {}°'.format(angulo))
print(' Seno | Cosseno | Tangente ')
print('{:^6.2f}|{:^9.2f}|{:^10.2f}'.format(sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
