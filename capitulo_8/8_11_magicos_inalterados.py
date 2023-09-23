def show_magicians(magicians):
    """Exibe o nome de cada mágico na lista."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Modifica a lista de mágicos acrescentando 'o Grande' ao nome de cada mágico."""
    great_magicians = []
    for magician in magicians:
        great_magicians.append("o Grande " + magician)        
    return great_magicians

# Lista inicial de mágicos
magicians = ['Harry Houdini', 'David Copperfield', 'Penn Jillette', 'Teller']

# Exibe a lista de mágicos sem modificação
print("Lista original de mágicos:")
show_magicians(magicians)

# Cria uma nova lista com a expressão 'o Grande' adicionada aos nomes de mágicos
great_magicians = make_great(magicians[:])

# Exibe a lista de mágicos modificada
print("\nLista de mágicos modificada:")
show_magicians(magicians)

# Exibe a nova lista de mágicos com a expressão 'o Grande' adicionada
print("\nNova lista de mágicos com 'o Grande' adicionado:")
show_magicians(great_magicians)

