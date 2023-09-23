def show_magicians(magicians):
    """Exibe o nome de cada mágico de uma lista"""
    for magician in magicians:
        print(magician.title())
        
magicians = ['Harry Houdini', 'David Copperfield', 'Penn Jillette', 'Teller']
show_magicians(magicians)
