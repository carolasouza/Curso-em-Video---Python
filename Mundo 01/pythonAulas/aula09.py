# Trabalhando com cadeia de caracteres
frase = 'Curso em Vídeo Python'

print('-'*10)
print('-Formas de Fatiamento-')
print(frase[9])
print(frase[9:14])
print(frase[9:21:2]) #adicionando passo do fatiamento
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print('-'*10)
print('-Análise-')
print(type(frase))
print(len(frase))
print(frase.count('o')) #quantas letras 'o' aparecem
print(frase.count('o', 0, 13)) #quantas letras 'o' aparecem entre o índice 0 e 13
print(frase.find('deo')) #se o trecho de strings for encontrado, será apresentado o índice da primeira letra
print(frase.find('Android')) #o '-1' indica que o trecho de strings não foi encontrado no conjunto de caracteres
print('Curso' in frase) #operador booleano
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower()) #os métodos utilizam parenteses ()
print(frase.capitalize())
print(frase.title())
print(frase.lower().find('vídeo'))

frase2 = '   Aprenda Python  '
print(frase2, '-', len(frase2))
print(frase2.strip(), '-', len(frase2.strip())) #remove os espaços nas extremidades do conjunto de caracteres
print(frase2.rstrip(), '-', len(frase2.rstrip())) #remove os espaços do lado DIREITO (right) do conjunto de caracteres

print('-'*10)
print('-DIVISÃO-')
print(frase.split()) #gera uma lista com todas as palavras, separadas por espaços, de uma cadeia de caracteres

print('-'*10)
print('-DIVISÃO-')
print('-'.join(frase.split()))

print(""" Ipsum is simply dummy text of the printing and typesetting 
industry. Lorem Ipsum has been the industry's standard dummy text
ever since the 1500s, when an unknown printer took a galley of 
type and scrambled it to make a type specimen book. It has 
survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. """)

# a string é IMUTÁVEL. para alterá-la, devemos utilizar a atribuição novamente.
