prompt = input("Qual a sua idade?")
active = True

while active:
    age = int(prompt)
    if age <= 3:
        print("Sua entrada é gratuita.")
        active = False
    elif age > 3 and age <= 12:
        print("Sua entrada custa R$ 10.")
        active = False
    else:
        print("Sua entrada custa R$ 15.")
        active = False
        
