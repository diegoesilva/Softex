#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir dessas informações, o sistema 
#mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor 
#correto seja preenchido.


while True:
    
    try:
        nome = input("\nInforme seu nome: ")
        dn = int(input("Informe sua data de nascimento: "))
        if dn <1922 or dn >2021:
            raise Exception("Idade fora dos parâmetros esperados. O ano de nascimento deve estar entre 1922 e 2021.")
        else:
            print(f"{nome}, você tem atualmente ", 2022-dn," anos.")
            break
    except Exception as err:
        print("\nOcorreu um erro: ", err)
        print("\nPor favor, tente novamente.")
