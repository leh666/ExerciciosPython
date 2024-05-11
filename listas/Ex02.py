lista=[]

qtd=int(input("quantos numeros: "))
for i in range(qtd):
    numero_digitado = int(input())
    lista.append(numero_digitado)
par=[]
impar=[]
for numero in lista:
    if numero % 2==0:
        par.append(numero)
    else:
        impar.append(numero)

print("Lista completa:", lista)
print("Pares:", par)
print("Impares:", impar)
