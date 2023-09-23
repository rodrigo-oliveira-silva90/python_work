def describe_city(city, country='brasil'):
    """Exibe a cidade e seu país"""
    print(city.title() + " está localizada no " + country.title() + ".")
    
describe_city('atibaia')
describe_city('campinas')
describe_city(city='Paris', country='França')
