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

def test_01():
    assert intercala([1,2],[3,4],[5,6]) == [1,3,5,2,4,6]

def test_02():
    assert intercala([0,0],[1,1],[2,2]) == [0,1,2,0,1,2]
          
def test_03():
    assert intercala([9,0],[6,2],[1,1])==[9,6,1,0,2,1]



    





    
