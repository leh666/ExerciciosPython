import math 
tamanho_mts_quad=float(input("qual tamanho em metros quadrados da area a ser pintada: "))
valor_diario=float(input("valor da tinta na data de hoje: "))
litros_de_tinta=tamanho_mts_quad/3
qtd_latas=math.ceil(litros_de_tinta/30)
custo=qtd_latas*valor_diario

print("quantidade de latas e: ", qtd_latas )
print("valor total de: ", custo)
