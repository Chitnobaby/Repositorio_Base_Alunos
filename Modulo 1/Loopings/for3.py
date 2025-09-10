
palavra = input("Digite uma palavra: ")
vogais = "aeiou"

# if  vogais in palavra:
#     print('Quantidade de vogais:')
# else:
#     print('nao existe')

for item in 'palavra':
    print(item in vogais)
