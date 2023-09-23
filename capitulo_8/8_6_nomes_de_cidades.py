def city_country(city, country):
    """Exibe o nome da cidade e seu país formatado."""
    full_name = city + ", " + country
    return full_name.title()
    
cidade1 = city_country ('santiago','chile')
cidade2 = city_country('rio de janeiro','brasil')
cidade3 = city_country('lima','peru')

print(cidade1)
print(cidade2)
print(cidade3)

