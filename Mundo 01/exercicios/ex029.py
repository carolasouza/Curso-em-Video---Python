print('===== DESAFIO 29 =====')
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

print('-'*50)
print(f'{"Limite de velocidade do veículo":^50}')
print('-'*50)

velocidade = float(input('\nQual a velocidade do carro neste momento em Km/h?: '))
if velocidade > 80:
    print('\nVocê está acima da velocidade permitida! Tome cuidado!')
    print('Você receberá uma multa no valor de R${:.2f}.'.format((velocidade - 80) * 7))
else:
    print('\nA velocidade está dentro do permitido!\nBoa viagem e dirija com segurança!')
