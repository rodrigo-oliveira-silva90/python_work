def make_shirt(shirt_message='eu amo python', shirt_size='G'):
    """Exibe o informações sobre camisetas estampadas"""
    print("\nCamiseta tamanho " + shirt_size + " e, estampada com a frase " + shirt_message.title() + ".")
    

make_shirt()
make_shirt(shirt_size='M')
make_shirt(shirt_size='P', shirt_message='eu falei que vinha')
