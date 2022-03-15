print('===== DESAFIO 11 =====')
print('Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de '
      'tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m²')

lar = float(input('\nDigite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = alt * lar
tinta = area / 2

print('\nCom dimensões de {}m x {}m, sua parede tem área igual a {}m².'.format(lar, alt, area))
print('Para pintar esta parede, você vai precisar de {}L de tinta.'.format(tinta))
