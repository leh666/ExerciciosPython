

altura=float(input("qual sua altura em metros: "))
sexo=input("f ou m: ")

if sexo=="f" or sexo=="F":
    peso_ideal= (62.1*altura)-44.7
elif sexo=="m" or sexo=="M": 
    peso_ideal=(72.7*altura)-58
else:
    print("erro, digite f ou m: ")
    quit()

print("seu peso ideal e: ",peso_ideal, "kg" )