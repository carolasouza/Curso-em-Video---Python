print('===== DESAFIO 09 =====')
print('Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.')
num = int(input('\nDigite um número inteiro: '))

print('\n------------\nTabuada do {}\n------------'.format(num))
i: int = 1
while 0 <= i <= 10:
    print('{:<2} x {:>2} = {}'.format(i, num, i * num))
    i += 1
print('-'*12)
