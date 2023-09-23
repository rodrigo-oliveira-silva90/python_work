responses = {}

polling_active = True

while polling_active:
    name = input("\nQual é o seu nome? ")
    response = input("Se pudesse visitar um lugar no mundo, para onde você iria? ")
    
    responses[name] = response
    
    repeat = input("Você gostaria que outra pessoa respondesse a pesquisa? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
print ("\n--- Resultados ---")
for name, response in responses.items():
    print(name.title() + " gostaria de visitar " + response.title() + ".")
