
valor_s=float(input("qual valor do saque: "))
n_100= valor_s //100
valor_s=valor_s % 100
n_50=valor_s //50
valor_s=valor_s % 50
n_20=valor_s //20
valor_s=valor_s % 20
n_10=valor_s //10
valor_s=valor_s % 10
n_5=valor_s // 5
valor_s=valor_s % 5
n_1=valor_s //1
valor_s=valor_s % 1
if n_100 !=0:
    print(int(n_100), "nota(s) de 100")
if n_50 !=0:
    print(int(n_50),"nota(s) de 50")
if n_20 !=0:
    print(int(n_20),"nota(s) de 20")
if n_10 !=0:    
    print(int(n_10),"nota(s) de 10")
if n_5 !=0:    
    print(int(n_5),"nota(s) de 5")
if n_1 !=0:   
    print(int(n_1),"nota(s) de 1")
        



