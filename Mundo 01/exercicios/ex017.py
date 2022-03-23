from math import hypot
print('===== DESAFIO 17 =====')

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo,
# calcule e mostre o comprimento da hipotenusa

catoposto = float(input('\nDigite a medida do cateto oposto: '))
catadjacente = float(input('Digite a medida do cateto adjacente: '))
print('\nPara um triângulo com: \nCateto oposto = {} e\nCateto adjacente = {}'
      '\nA hipotenusa será = {:.2f}'.format(catoposto, catadjacente, hypot(catoposto, catadjacente)))
