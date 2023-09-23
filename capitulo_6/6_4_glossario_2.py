glossario = {
    'variável':'Toda variável armazena um valor, que é a informação associada a essa variável',
    'string': 'Uma string é simplesmente uma série de caracteres',
    'lista': 'Uma lista é uma coleção de itens em uma ordem em particular',
    'identar': 'Forma de organizar o código',
    'tupla': 'Lista imutável',
    'dicionário': 'Dispositivo utilizado para conectar informações relacionadas',
    }
    
for palavra, significado in glossario.items():
    print("A palavra " + palavra.title() +  " significa:" + significado + ".\n")
