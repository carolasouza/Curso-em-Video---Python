print('===== DESAFIO 12 =====')
print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')

preco = float(input('\nDigite o preço do produto: R$'))
desconto = 5/100

print('\nDesconto: {}%\nPreço com desconto: R${:.2f}'.format(desconto * 100, preco * (1 - desconto)))
