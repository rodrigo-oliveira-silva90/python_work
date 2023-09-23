class User():
    
    def __init__(self, first_name, last_name, city, country, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.country = country
        self.age = age
        self.login_attempts = 0
        
    def describe_user(self):
        print("Resumo das informações do usuário:")
        print("\nNome: " + self.first_name.title())
        print("Sobrenome: " + self.last_name.title())
        print("Cidade: " + self.city.title())
        print("Pais: " + self.country.title())
        print("Idade: " + str(self.age))
        print("Tentativas de login: " + str(self.login_attempts) + "\n")
        
    def greet_user(self):
        print("Olá, " + self.first_name.title())
        
    def increment_login_attempts(self, logins):
        self.login_attempts += logins
        
    def reset_login_attempts(self):
        self.login_attempts = 0

        
        
user1 = User('rodrigo', 'silva', 'atibaia', 'brasil', 33)
user2 = User('bruna', 'lisboa', 'atibaia', 'brasil', 29)
user3 = User('lucas', 'maia', 'santo andré', 'brasil', 31)
user4 = User('isadora', 'maia', 'são paulo', 'brasil', 28)

user1.describe_user()

user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.reset_login_attempts()
user1.increment_login_attempts(1)

user1.describe_user()

