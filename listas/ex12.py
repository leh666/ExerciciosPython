from ex12_conta_alunos_baixos import conta_alunos_baixos
alturas=[]
idades=[]
for i in range(3):
    idade=int(input("digite uma idade: "))
    idades.append(idade)
    altura=int(input("digite uma altura: "))
    alturas.append(altura)
contagem = conta_alunos_baixos(alturas,idades)
print("numero de alunos abaixo da media:", contagem)
