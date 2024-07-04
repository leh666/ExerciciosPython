def soma_mult (lista):
    soma=0
    mult=1
    for item in lista:
        soma=soma + item
        mult=mult * item
    return [soma,mult]

def test_soma_mult_uns():
    assert soma_mult([1,1,1,1,1]) == [5,1]

def test_soma_mult_simples():
    assert soma_mult

def test_soma_mult_vazio():
    assert soma_mult()