

idades=[]
alturas=[]
for i in range (5):
    idade= int(input("qual a idade: "))
    idades.append(idade)
    altura= int(input("qual a altura: "))
    alturas .append(altura)

for i in range(4,-1,-1):
    altura=alturas[i]
    idade=idades[i]
    print("altura:",altura, "idade: ",idade)


    
