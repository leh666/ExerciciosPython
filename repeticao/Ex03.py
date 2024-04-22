
nome=input("informe o nome: ")
while len(nome) <= 3:      
    nome=input("digite um nome valido")
idade=int(input("digite a idade: "))
while not (idade >= 0 and idade <= 150):
    idade=int(input("digite a idade: "))
salario=float(input("digite o salario: "))
while salario <= 0:
    salario=float(input("digite o salario: "))
sexo=input("digite sexo f ou m: ")
while not (sexo=="f" or sexo=="m"):
    sexo=input("digite sexo f ou m: ")
estado_c=input("estado civil s, c, v, d: ")
while not (estado_c== "s" or estado_c== "c" or estado_c== "v" or estado_c== "d"):
    estado_c=input("estado civil s, c, v, d: ")


    


