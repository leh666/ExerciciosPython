
nome=input("informe o nome: ")
sen=input("digite uma senha: ")
while sen == nome or len(sen) < 8:
    sen=input("invalido, por favor digite nova senha: ")
print("valido")

