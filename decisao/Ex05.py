nota_1=float(input("digite primeira nota: "))
nota_2=float(input("segunda nota: "))
media=(nota_1+nota_2)/2
if media==10:
    print("Aprovado com Distinção")
        
elif media < 7:
    print("reprovado")
elif media >= 7:
    print("aprovado")

