def make_sandwichs(*ingredientes):
    """Exibe uma lista de ingredientes para sanduíches"""
    print("\nfazer o sanduíche com os seguintes ingredientes:")
    for ingrediente in ingredientes:
        print("-" + ingrediente)
        
make_sandwichs('carne', 'queijo')
make_sandwichs('presunto', 'queijo', 'tomate')
make_sandwichs('peito de peru', 'alface', 'maionese', 'mostarda') 
