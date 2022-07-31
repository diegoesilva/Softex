# Estruture três códigos, os quais devem conter uma função de manipulação de
# string que obtenha resultado.

# Código 1 - Informa a quantidade de caracteres na string

print(len(input("\nEscreva qualquer coisa: ")))

# Código 2 - Recebe uma string e converte para maiúsculas

print(input("\nEscreva qualquer coisa: ").upper())

# Código 3 - Recebe uma string e mostra de trás pra frente

string = input("\nEscreva qualquer coisa: ")

for i in range(len(string), 0, -1):
    print(string[i-1], end = "")
