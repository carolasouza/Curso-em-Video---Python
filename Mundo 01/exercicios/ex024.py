print('===== DESAFIO 24 =====')
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input("\nDigite o nome de uma cidade: ")).strip() #eliminando os espaços nas extremidades
print('santo' in cidade.lower()[0:5])
print(cidade.lower()[0:5] == 'santo')
