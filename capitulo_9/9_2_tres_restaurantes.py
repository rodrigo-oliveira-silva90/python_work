class Restaurant():
    """Exibe informações sobre um restaurante"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("\nO restaurant " + self.restaurant_name.title() + " serve comida " + self.cuisine_type + " com um toque moderno.")
        
    def open_restaurant(self):
        print("\nO restaurante " + self.restaurant_name.title() + " está aberto.")
        
primeiro_restaurante = Restaurant('la trattoria', 'italiana')
segundo_restaurante = Restaurant('mocotó', 'brasileira')
terceiro_restaurante = Restaurant('le president', 'francesa')

primeiro_restaurante.describe_restaurant()
segundo_restaurante.describe_restaurant()
terceiro_restaurante.describe_restaurant()

        
