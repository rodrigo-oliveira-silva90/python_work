def make_shirt(shirt_size, shirt_message):
    """Exibe o informações sobre camisetas estampadas"""
    print("\nCamiseta tamanho " + shirt_size + " e, estampada com a frase " + shirt_message.title() + ".")
    

make_shirt('M', 'eu falei que vinha')
make_shirt(shirt_message='eu falei que vinha', shirt_size='M')
