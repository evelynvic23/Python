# //Fingir que existe uma função

# Eu crio a função e tenho como parâmetro a variável que armazena o número
def primo_mentirinha(numero):
    # Crio uma variável que contabiliza a quantidades de divisores
    quantidade_divisores = 0
    # o for é responsável por contabilizar os divisores
    for p in range(1, numero+1):
        if numero % p == 0:
            quantidade_divisores += 1
    if quantidade_divisores == 3:
        return True
    else: 
        return False

numero = int(input())
if primo_mentirinha(numero):
    print('sim')
else:
    print('nao')