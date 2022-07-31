# Estruture três códigos, os quais devem conter uma função de manipulação de
# string que obtenha resultado.

print("CÓDIGO 1 - Informa a quantidade de caracteres na string\n")

def contar(string):
    return len(string)

print(contar(input("Escreva uma palavra ou frase para ser contada: ")), "caracteres.")




print("\nCÓDIGO 2 - Recebe uma string e converte para maiúsculas\n")

def cxAlta(string):
    return string.upper()

print("Entrada convertida:", cxAlta(input("Escreva algo para ser convertido: ")))

print("\nCÓDIGO 3 - Recebe uma string e mostra de trás pra frente\n")

def reverso(string):
    rev = ""
    for i in range(len(string), 0, -1):
        rev += string[i-1]
    return rev

print("Entrada revertida:", reverso(input("Escreva algo para ser revertido: ")))
    
