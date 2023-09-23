def show_magicians(magicians):
    """Exibe o nome de cada mágico na lista."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Modifica a lista de mágicos acrescentando 'o Grande' ao nome de cada mágico."""
    for i in range(len(magicians)):
        magicians[i] = "o Grande " + magicians[i]

# Lista inicial de mágicos
magicians = ['Harry Houdini', 'David Copperfield', 'Penn Jillette', 'Teller']

# Exibe a lista de mágicos sem modificação
print("Lista original de mágicos:")
show_magicians(magicians)

# Modifica a lista de mágicos
make_great(magicians)

# Exibe a lista de mágicos modificada
print("\nLista de mágicos modificada:")
show_magicians(magicians)
