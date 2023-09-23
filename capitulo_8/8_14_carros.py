def make_car(fabricante, modelo, **car_info):
    """Constrói um dicionário com informações dos carros."""
    profile = {}
    profile['fabricante'] = fabricante
    profile['modelo'] = modelo
    for key, value in car_info.items():
        profile[key] = value
    return profile
    
car = make_car('subaru', 'outback', color='black', tow_package=True)

print(car)
