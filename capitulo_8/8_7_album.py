def make_album(artista, album, faixas=''):
    """Devolve um dicionário com informações do albúm."""
    album = {'criador':artista, 'nome':album}
    if faixas:
        album['faixas'] = faixas
    return album
    
album1 = make_album('o rappa', 'pescador de ilusões')
album2 = make_album('nirvana', 'nevermind')
album3 = make_album('charlie brown jr', 'pontes indestrutíveis')
album4 = make_album('o rappa', 'lado a lado b', 10)

print(album1)
print(album2)
print(album3)
print(album4)

