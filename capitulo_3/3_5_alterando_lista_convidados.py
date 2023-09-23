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

