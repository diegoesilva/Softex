#Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter a seguinte estrutura:

#aluno: Nome do aluno;
#nota_1: Primeira nota;
#nota_2: Segunda nota;
#faltas: Número de faltas;

#O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas do aluno. 
#A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

#O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo dataframe com 
#o nome “alunos_situacao.csv”.

#Por fim, o programa deverá mostrar na tela:
#- o maior número de faltas;
#- a média geral das notas dos alunos;
#- e a maior média.


import pandas as pd

df = pd.read_csv("notas_alunos.csv")

media = (df["nota_1"]+df["nota_2"])/2
df["media"] = media

if df["faltas"] > 5 or df["media"] < 7:
  df["situacao"] = "Reprovado"
else:
  df["situacao"] = "Aprovado"

df.to_csv('alunos_situacao.csv')

maiorFaltas = df["faltas"].max()
mediaGeral = df["media"].median()
maiorMedia = df["media"].max()

print(f"\nO maior número de faltas foi {maiorFaltas}")
print(f"\nA média geral dos alunos foi {mediaGeral}")
print(f"\nA maior média foi {maiorMedia}")
