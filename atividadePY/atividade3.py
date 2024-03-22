# Evelyn Victoria da Silva Santos

km = float(input("Digite os quilômetros percorridos: "))


combustivel = float(input("Digite o combústivel consumido: "))

div = km / combustivel

if div <= 8:
    print("O automóvel está consumindo muito combustível")
else:
    print("O consumo está bom")