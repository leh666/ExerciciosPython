valor_saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

if valor_saque < 10 or valor_saque > 600:
    print("Valor inválido. O saque deve ser entre 10 e 600 reais.")
else:
    notas_100 = valor_saque // 100
    valor_saque %= 100

    notas_50 = valor_saque // 50
    valor_saque %= 50

    notas_10 = valor_saque // 10
    valor_saque %= 10

    notas_5 = valor_saque // 5
    valor_saque %= 5

    notas_1 = valor_saque

    if notas_100 > 0:
        print("Notas de 100: ", notas_100)
    if notas_50 > 0:
        print("Notas de 50: ", notas_50)
    if notas_10 > 0:
        print("Notas de 10: ", notas_10)
    if notas_5 > 0:
        print("Notas de 5: ", notas_5)
    if notas_1 > 0:
        print("Notas de 1: ", notas_1)