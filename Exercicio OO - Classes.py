#Crie uma classe de sua preferência com, no mínimo, uma variável, um método e
#um incremento. Depois, desenvolva três ou mais objetos para testar o código.

class Profissional:
    def __init__(self, nome, profissão, salário):
        self.nome = nome
        self.profissao = profissão
        self.salario = salário

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e eu sou {self.profissao}.")
    
    def aumentarSalario(self, valor = 1000):
        self.salario += valor
        print(f"O salário de {self.nome} agora é de {self.salario}!")

    
prof1 = Profissional("Prad Bitt", "ator", 5000)
prof2 = Profissional("Melon Usk", "empresário", 120000)
prof3 = Profissional("Huciano Luck", "apresentador", 1500)


prof1.apresentar()
print(f"{prof3.nome} recebia {prof3.salario}...")
prof3.aumentarSalario(3000)
