def intercala(lista1, lista2,lista3):
    interc=[]
    for i in range (2):
        e1=lista1[i]
        e2=lista2[i]
        e3=lista3[i]
        interc.append(e1)
        interc.append(e2)
        interc.append(e3)
    return interc

#inicio, pega elementos
elems1=[]
elems2=[]
elems3=[]
for i in range (2):
    elem= int(input())
    elems1.append(elem)
    elem= int(input())
    elems2.append(elem)
    elem= int(input())
    elems3.append(elem)

#miolo
inter = intercala(elems1,elems2,elems3)

#final, printar
print(inter)




    





    
