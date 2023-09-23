def make_album(artista, album, faixas=''):
    """Devolve um dicionário com informações do albúm."""
    album = {'criador':artista, 'nome':album}
    if faixas:
        album['faixas'] = faixas
    return album
    
while True:
    print("\nInsira as informações do albúm")
    print("(digite 'q' a qualquer momento para sair)")
    
    f_name = input("Nome do artista: ")
    if f_name == 'q':
        break
        
    l_name = input("Nome do albúm: ")
    if l_name == 'q':
        break
        
    formatted_name = make_album(f_name, l_name)
    print(formatted_name)
    

