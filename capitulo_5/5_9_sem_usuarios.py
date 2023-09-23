usuarios = ['admin','rodrigo','bruna','ana','gabriel','silvana']

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print("Olá " + usuario.title() + ", gostaria de ver um relatório de status?")
        else:
            print("Olá " + usuario.title() + ", obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar alguns usuários!")
