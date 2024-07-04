
temperaturas_mes=[]
meses=["janeiro", "fevereiro","marco", "abril", "maio", "junho", "julho", "agosto", "setembro","outubro","novembro", "dezembro"]
for i in range(12):
   temp=float(input("digite temperatura de " + meses[i]+": ")) 
   temperaturas_mes.append(temp)
soma=0
for i in range(12):
   temp=temperaturas_mes[i]
   soma=soma+temp
media=soma/12
for i in range(12):
   temp=temperaturas_mes[i]
   if temp>media:
      print (temp, meses[i] )

