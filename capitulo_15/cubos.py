import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s=40)

# Define o título do gráfico e nomeia os eixos
plt.title("Cub Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cub of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo
plt.axis ([0,5100,0,125000000000])

plt.show()

