nota_1=float(input("digite primeira nota: "))
nota_2=float(input("segunda nota: "))
media=(nota_1+nota_2)/2
if media >= 9 and media <= 10:
    conceito="A"
elif media >= 7.5 and media < 9:
    conceito="B"
elif media >= 6 and media < 7.5:
    conceito="C"
elif media >= 4 and media < 6:
    conceito="D"
else:
    conceito="E"


if conceito=="A" or conceito== "B" or conceito== "C":
    msg_aprovado_ou_reprovado="aprovado"  
else:
    msg_aprovado_ou_reprovado="reprovado"
print(nota_1, nota_2, media, conceito,msg_aprovado_ou_reprovado)

        



