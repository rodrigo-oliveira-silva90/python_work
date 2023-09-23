favorite_numbers = {
    'rodrigo': [7, 19, 23],
    'bruna': [5, 7, 11],
    'gabriel': [4, 15, 23], 
    'silvana': [11, 22, 35],
    'ana': [5, 15, 20],
    }
    
for nome, numeros in favorite_numbers.items():
    print("\n Os números favoritos de " + nome.title() + " são:")
    for numero in numeros:
        print("\t" + str(numero))
