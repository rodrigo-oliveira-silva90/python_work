prompt = "\nInforme um ingrediente para adicionar na sua pizza:"
prompt += "\nDigite 'quit' para encerrar."

message = ""
while message != 'quit':
    message = input(prompt)
    print("O ingrediente " + message + " foi adicionado.")
    
