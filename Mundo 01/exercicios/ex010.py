print('===== DESAFIO 10 =====')
print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.')

real = float(input('\nQuanto dinheiro você tem na sua carteira? R$'))

print('\nCom R${:.2f} você pode comprar U${:.2f}.'.format(real, real/5.10))
print('Com R${:.2f} você pode comprar €{:.2f}.'.format(real, real/5.77))
