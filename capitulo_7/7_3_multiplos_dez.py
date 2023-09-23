numero = input("Informe um número: ")
numero = int(numero)

if numero % 10 == 0:
    print("\n O número " + str(numero) + " é múltiplo de dez.")
else:
    print("\n O número " + str(numero) + " não é múltiplo de dez.")
