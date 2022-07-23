#Desenvolva um código que simule uma eleição com três candidatos.
#- candidato_X => 889
#- candidato_Y => 847
#- candidato_Z => 515
#- branco => 0

#O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda a nenhum candidato ou seja branco, ele deve ser tratado
#como nulo. Se for inserido um texto ao invés de número, o código deve retornar uma mensagem para votar novamente.

#Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a quantidade de votos de cada candidato, os
#brancos e nulo


print("ELEIÇÕES")

cand_X = 0
cand_Y = 0
cand_Z = 0
brancos = 0
nulos = 0

try:
    while True:
        print("\nCandidato X => 889\nCandidato Y => 847\nCandidato Z => 515\nBranco      => 0\n")
        escolha = input("Por favor, digite o número do candidato desejado: ")

        if escolha.isalpha():
            print("Você deve digitar apenas números.")
            pass
        else:
            if escolha == "889":
                cand_X += 1
            elif escolha == "847":
                cand_Y += 1
            elif escolha == "515":
                cand_Z += 1
            elif escolha == "0":
                brancos += 1
            else:
                nulos += 1
        
            finalizar = input("\nVoto computado. Deseja votar novamente? Digite 's' para sim. Caso contrário, precione qualquer outra tecla: ").lower()
            if finalizar != "s":
                break
            else:
                print("\nMuito bem, vote novamente.")
    
except:
    pass

candidatos = ["Candidato X", "Candidato Y", "Candidato Z", "Brancos", "Nulos"]
resultado = [cand_X, cand_Y, cand_Z, brancos, nulos]
vencedor = candidatos[resultado.index(max(resultado))]

print("\nVotação encerrada.")
print(f"\nRESULTADO:\n\nCandidato X: {cand_X} votos\nCandidato Y: {cand_Y} votos\nCandidato Z: {cand_Z} votos\nVotos Brancos: {brancos}\nVotos Nulos: {nulos}")
print(f"\nVencedor: {vencedor}!")


