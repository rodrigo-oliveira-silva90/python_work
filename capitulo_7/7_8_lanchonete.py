sandwich_orders = ['cheeseburguer','club sandwich', 'bauru', 'blt', 'veggie sandwich', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("\nA lanchonete está pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print("Preparei seu sanduíche " + current_sandwich.title())
    finished_sandwiches.append(current_sandwich)
    
print ("\nOs seguintes sanduíches estão prontos:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
