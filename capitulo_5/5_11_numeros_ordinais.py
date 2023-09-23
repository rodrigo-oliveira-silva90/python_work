numeros = list(range(1,10))

for numero in numeros:
    if numero == 1:
        print(str(numero) + "st")
    if numero == 2:
        print(str(numero) + "nd")
    if numero == 3:
        print(str(numero) + "rd")
    if numero >= 4:
        print(str(numero) + "th")
