def funcao_soma (lista):
    soma=0
    for item in lista:
        soma=soma + item
    return soma

def funcao_mult (lista):
    mult=1
    for item in lista:
        mult=mult * item
    return mult

print("Digite 5 numeros:")
lista_digitada=[]
for i in range(5):
    elem=int(input())
    lista_digitada.append(elem)  

soma = funcao_soma(lista_digitada)
mult = funcao_mult(lista_digitada)

print("soma:", soma)
print("mult",mult)
print(lista_digitada)

