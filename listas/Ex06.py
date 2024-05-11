lst_media=[]

qtd_alunos=int(input("quantidade de alunos: "))

# Para cada aluno...
for i in range(qtd_alunos):
    print("Digite 4 notas para o aluno #", i, ":")
    media = 0
    # Peça as 4 notas...
    for j in range(4):
        nota_dgt = float(input())
        media = media + nota_dgt
    media = media / 4    
    lst_media.append(media)

contador=0    

print("Alunos com media maior igual a 7:")

for media in lst_media:
    if media >= 7:
        print (media)   
        contador = contador +1

print("Total de alunos que passaram:", contador)
