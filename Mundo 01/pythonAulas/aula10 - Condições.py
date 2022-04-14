# Condições

# tempo = int(input('Quantos anos tem seu carro? '))
# print('Carro novo!' if tempo <= 3 else 'Carro velho!')
# print('--- FIM ---')

# nome = str(input('Digite seu nome: '))
# if nome == 'Carol':
#     print('Que nome lindo você tem!')
# else:
#     print('Tudo bem, {}?'.format(nome))
# print('Bom dia, {}!'.format(nome))

print('-----Cálculo da média do aluno-----')
n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('\nMédia do aluno: {:.2f}'.format(m))
print('Nota acima da média. PARABÉNS!' if m >= 6 else 'Nota abaixo da média. ESTUDE MAIS!')
print('----- FIM -----')
