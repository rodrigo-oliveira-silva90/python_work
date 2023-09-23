pizzas = ['portuguesa', 'mussarela', 'pepperoni']
friend_pizzas = pizzas[:]

pizzas.append ('calabresa')
friend_pizzas.append ('baiana')

print("Minhas pizzas favoritas são:")

for pizza in pizzas:
	print(pizza)

print("\nAs pizzas favoritas de meu amigo são:")

for pizza in friend_pizzas:
	print(pizza)
