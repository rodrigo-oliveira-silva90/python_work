cities = {
    'nova york': {
    'country': 'estados unidos', 
    'population': 20140470, 
    'fato': 'Astoria é o bairro com mais brasileiros',
        },
        
    'paris': {
    'country': 'frança', 
    'population': 12532901, 
    'fato': 'Primeira grande cidade européia a utilizar iluminação a gás',
        },
        
    'lagos' : {
    'country': 'nigéria', 
    'population': 7937932, 
    'fato': 'Segunda maior cidade africana'
        },
    }
    
for cidade, infos in cities.items():
    print("\n Cidade: " + cidade.title())
    
    country = infos['country']
    population = infos['population']
    fact = infos['fato']
    
    print("\tCountry: " + country.title())
    print("\t Population: " + str(population))
    print("\tFact: " + fact)
