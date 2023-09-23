class Restaurant():
    """Exibe informações sobre um restaurante"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("\nO restaurant " + self.restaurant_name.title() + " serve comida " + self.cuisine_type + " com um toque moderno.")
        
    def open_restaurant(self):
        print("\nO restaurante " + self.restaurant_name.title() + " está aberto.")
        
my_restaurant = Restaurant('la trattoria', 'italiana')

my_restaurant.describe_restaurant()

my_restaurant.open_restaurant()
        
