from random import randint
from time import sleep
print('===== DESAFIO 28 =====')
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('-'*25)
print(f'{"JOGO DE ADIVINHAÇÃO":^25}')
print('-'*25)

num = randint(0, 5) #Faz o computador "PENSAR"
print('\nPENSANDO... em um número (inteiro, entre 0 e 5)...')
adivinha = int(input('Tente adivinhar o número que escolhi: ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)

if adivinha == num:
    print('\nAcho que temos um Sherock Homes por aqui.. PARABÉNS!')
    print('Eu pensei no número {} e você adivinhou.'.format(num))
else:
    print('\nÉ, você PERDEU!')
    print('Eu pensei no número {} e você achou que era o {}.\nTente outra vez.'.format(num, adivinha))
