print('=' * 5, end=' ')
print('DESAFIO 15', end=' ')
print('=' * 5)

print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a '
      'quantidade de dias pelos quais ele foi alugado. '
      '\nCalcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.')

dias = int(input('\nPor quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram percorridos? '))

preco = 60 * dias + 0.15 * km

print('\nPreço a pagar: R${:.2f}'.format(preco))

