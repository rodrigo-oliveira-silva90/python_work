favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil' : 'python',
    }
    
responderam = ['phil', 'sarah']

for name in favorite_languages.keys():
       
    if name in responderam:
        print(name.title() + ", obrigado por responder a pesquisa.")
    else:
        print(name.title() + ", gostaria de convidá-lo a responder a pesquisa.")
