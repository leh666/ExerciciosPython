respostas=[]
pergutas=["Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?"]
for i in pergutas:
    resposta=int(input(i))
    respostas.append(resposta)
cont=0
for resposta in respostas:
    if resposta == 1:
        cont=cont+1
if cont== 2:
    print("Suspeito")
if cont== 3 or cont== 4:
    print("cumplice")
if cont== 5:
    print("Assassino")
else:
    print("inocente")




