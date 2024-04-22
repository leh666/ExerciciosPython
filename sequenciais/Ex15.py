ganho_hora=float(input("ganhos por horas trabalhadas: "))
horas_mes=int(input("horas trabalhadas no mes: ")) 
total=ganho_hora*horas_mes 
ir=11/100*total
inss=8/100*total
sind=5/100*total
liquido=total-ir-inss-sind
print("+ Salário Bruto : R$", total)  
print("- IR (11%) : R$", ir)
print("- INSS (8%) : R$", inss)
print("- Sindicato ( 5%) : R$", sind)     
print("= Salário Liquido : R$", liquido)