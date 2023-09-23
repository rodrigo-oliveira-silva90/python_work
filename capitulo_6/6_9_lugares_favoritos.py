favorite_places = {
    'bruna': ['são paulo', 'atibaia', 'paris'],
    'rodrigo': ['são paulo', 'buenos aires', 'maceió'],
    'gabriel': ['itu', 'uberaba', 'atibaia']
    }
    
for nome, lugares in favorite_places.items():
    print("\n Os lugares favoritos de " + nome.title() + " são:")
    for lugar in lugares:
        print("\t" + lugar.title()) 
