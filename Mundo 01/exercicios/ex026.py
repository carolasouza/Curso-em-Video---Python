print('===== DESAFIO 26 =====')
# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez

frase = str(input('\nDigite uma frase: ').strip().upper())
print('\n- A letra "A" aparece {} vez(es)'.format(frase.count('A')))
print('- A primeira ocorrência é na {}ª posição'.format(frase.find('A')+1))
print('- A última ocorrência é na {}ª posição'.format(frase.rfind('A')+1))
