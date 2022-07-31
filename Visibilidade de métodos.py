#Crie uma classe e insira nela, no mínimo, dois atributos, os quais devem ter
#um método acessor (get) e um método modificador (set) para cada.
#Defina um objeto para cada atributo e elabore um construtor para criar alguma
#regra.

#A atividade pode ser realizada em qualquer linguagem de programação ou apenas utilizando algoritmos.




class Pessoa:
    def __init__(self, nome, idade):
        if len(nome.strip())>0:
            self.__nome = nome
        else:
            print("Nome inválido.")
        if idade>=0 and idade<=120:
            self.__idade = idade
        else:
            print("Idade inválida.")

    def getNome(self):
        return self.__nome
    def setNome(self, novoNome):
        if len(novoNome.strip())>0:
            self.__nome = novoNome
            print(f"Nome alterado para '{self.__nome}'.")
        else:
            print("Novo nome inválido.")

    def getIdade(self):
        return self.__idade
    def setIdade(self, novaIdade):
        if novaIdade>=0 and novaIdade<=120:
            self.__idade = novaIdade
            print(f"Idade alterada para {self.__idade}.")
        else:
            print("Idade inválida.")

### Instanciando...

pessoaUm = Pessoa("José", 71)
pessoaDois = Pessoa("Maria", 67)

### Tentando alterar atributos diretamente

pessoaUm.nome = "João"
pessoaDois.idade = 23

### Acessando atributos através dos métodos get

print("O nome da primeira pessoa é", pessoaUm.getNome())
print("A idade da segunda pessoa é", pessoaDois.getIdade(), "anos.\n")

### Alterando valores através dos métodos set

pessoaUm.setNome("Pedro")
pessoaDois.setIdade(32)

### Verificando alterações feitas, através do método get

print("\nO nome da primeira pessoa é", pessoaUm.getNome())
print("A idade da segunda pessoa é", pessoaDois.getIdade(), "anos.")
