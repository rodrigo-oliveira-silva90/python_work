current_users = ['caua','rodrigo','bruna','ana','gabriel','silvana']

new_users = ['Rodrigo','Bruna','camila']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Nome de usuário " + new_user + " já utilizado. Forneça um novo nome.")
    else:
        print("Nome de usuário " + new_user + " disponível.")
