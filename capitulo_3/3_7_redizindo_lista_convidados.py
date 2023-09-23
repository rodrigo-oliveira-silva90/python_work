lista_jantar = ['jesus', 'andré rebouças', 'cândido']
print('Sr. ' + lista_jantar[0].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n'
'Sr. ' + lista_jantar[1].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n'
'Sr. ' + lista_jantar[2].title() + ' gostaria de convidá-lo para um jantar em minha casa.')


nao_confirmado = lista_jantar.pop(0)
print('O convidado ' + nao_confirmado.title() + ' não confirmou o convite.')

lista_jantar.insert(0, 'cumpadi washington')

print('Sr. ' + lista_jantar[0].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n'
'Sr. ' + lista_jantar[1].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n'
'Sr. ' + lista_jantar[2].title() + ' gostaria de convidá-lo para um jantar em minha casa.')

print('Encontramos uma mesa de jantar maior. Por isso iremos convidar mais 3 pessoas.')

lista_jantar.insert(0,'noé')
lista_jantar.insert(2,'daniel')
lista_jantar.append('elias')

print('Sr. ' + lista_jantar[0].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n'
'Sr. ' + lista_jantar[1].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n'
'Sr. ' + lista_jantar[2].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n'
'Sr. ' + lista_jantar[3].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n'
'Sr. ' + lista_jantar[4].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n'
'Sr. ' + lista_jantar[5].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n')

print('Infelizmente a nova mesa de jantar não chegará a tempo para o jantar e teremos espaço para somente dois convidados.')

removido_0 = lista_jantar.pop()
print('Sr. ' +removido_0.title() + ',devido ao problema com a mesa, não poderei convidá-lo para o jantar.')

removido_1 = lista_jantar.pop()
print('Sr. ' +removido_1.title() + ',devido ao problema com a mesa, não poderei convidá-lo para o jantar.')

removido_2 = lista_jantar.pop()
print('Sr. ' +removido_2.title() + ',devido ao problema com a mesa, não poderei convidá-lo para o jantar.')

removido_3 = lista_jantar.pop()
print('Sr. ' +removido_3.title() + ',devido ao problema com a mesa, não poderei convidá-lo para o jantar.')

print('Sr. ' + lista_jantar[0].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n'
'Sr. ' + lista_jantar[1].title() + ' gostaria de convidá-lo para um jantar em minha casa.\n')

del lista_jantar[0]
del lista_jantar[0]

print(lista_jantar)


