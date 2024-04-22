print("CONVERSOR DE TEMPERATURA")

escolha=-1
while not (escolha==1 or escolha==2):
    print("1 - Fahrenhei para celcius ")
    print("2 - de celcius para Fahrenheit")
    print("0 - sair")

    escolha=int(input("digite: "))
    if escolha==1:  
        temp_graus_fh=float(input("qual temperatura em grau fahrenheit: "))
        c=5 *((temp_graus_fh-32) / 9)
        print("a temperatura em graus celcius e: ", c) 
    elif escolha==2:
        c=float(input("qual temperatura em grau celcius: "))
        f=9/5*c +32  
        print("a temperatura em graus fahrenheit e: ", f )
    elif escolha==0: 
        print("voce esta saindo do programa, obrigada!!!")  
        quit() 
    else:
        print("escolha uma das alternativas corretas: ")
    