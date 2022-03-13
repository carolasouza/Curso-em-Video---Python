print('===== DESAFIO 08 =====')
print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.')
num = float(input('\nDigite uma distância em metros: '))
km = num * 0.001
hm = num * 0.01
dam = num * 0.1
m = num * 1
dm = num * 10
cm = num * 100
mm = num * 1000
print('\n{}m = {}km'
      '\n{}m = {}hm'
      '\n{}m = {}dam'
      '\n{}m = {}m'
      '\n{}m = {}dm'
      '\n{}m = {}cm'
      '\n{}m = {}mm'.format(num, km, num, hm, num, dam, num, m, num, dm, num, cm, num, mm))
