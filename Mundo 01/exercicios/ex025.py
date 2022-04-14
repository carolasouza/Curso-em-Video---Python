import emoji
print('===== DESAFIO 25 =====')
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite seu nome completo: ').strip()
if not ('silva' in nome.lower()):
    print(emoji.emojize('Poxa, seu nome não tem "SILVA" :cry:', use_aliases=True))
else:
    print(emoji.emojize('Que legal, seu nome tem "SILVA"! :smiley:', use_aliases=True))

# print('silva' in nome.lower())
