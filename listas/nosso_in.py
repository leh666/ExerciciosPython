def nosso_in(elemento, lista):
    for j in lista:
        if j == elemento:
            return True
    return False

def le_lista():
    lista=[]
    elem="oi"
    while elem != "":
        elem= input()
        lista.append(elem)   
    return lista

alunos = le_lista()
aln_hj=input("digite o nome do aluno: ")
if nosso_in(aln_hj,alunos):
    print(aln_hj, "veio.")
else:
    print(aln_hj, "nao veio hoje.")



def test_nosso_in_simples():
    assert nosso_in(1, [1,2,3,4,5]) == True

def test_nosso_in_segundo():
    assert nosso_in(2, [1,2,3,4,5]) == True

def test_nosso_in_quinto():
    assert nosso_in(5, [1,2,3,4,5]) == True

def test_nosso_in_vazio():   
    assert nosso_in(7, []) == False

def test_nosso_in_string_naotem():
    assert nosso_in("a", "erick")==False

def test_nosso_in_string_tem():
    assert nosso_in("a", "allan")==True

