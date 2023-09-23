rios = {'amazonas' : 'brasil', 'sena' : 'frança', 'yellow river' : 'china',}

for rio, pais in rios.items():
    print("O " + rio.title() + " corre pelo " + pais.title() + ".\n")
    
for rio in rios.keys():
    print(rio.title())
    
print("\n")
    
for pais in rios.values():
    print(pais.title())
