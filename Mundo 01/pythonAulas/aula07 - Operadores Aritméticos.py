# nome = input('Qual o seu nome? ')
# print('Prazer em te conhecer {:<10}!'.format(nome))
# print('Prazer em te conhecer {:>10}!'.format(nome))
# print('Prazer em te conhecer {:=^10}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1//n2
e = n1 ** n2

# print('Soma: {}\nProduto: {}\nDivisão: {:.3f}\nDivisão inteira: {}\nPotência: {}'.format(s, m, d, di, e))

print('Soma: {}; Produto: {}; Divisão: {:.3f}; '.format(s, m, d), end='')
print('Divisão inteira: {}; Potência: {}'.format(di, e))
