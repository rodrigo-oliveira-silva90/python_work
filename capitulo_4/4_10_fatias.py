cubos = []
for valor in range(1,11):
	cubo = valor**3
	cubos.append(cubo)
	
print("Os três primeiros itens da lista são:")
print(cubos[0:3])

print("Os três itens do meio da lista são:")
print(cubos[4:7])


print("Os três últimos itens da lista são:")
print(cubos[-3:])
