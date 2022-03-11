print('===== DESAFIO 06 =====')
print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.\n')
num = int(input('Digite um número: '))
print('Dobro: {}\nTriplo: {}\nRaiz quadrada: {:.2f} ou {:.2f}'.format(num * 2, num * 3, num ** (1/2), pow(num, 1/2)))
