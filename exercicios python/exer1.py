# Enunciado para o fluxograma: Teorema de Pitágoras

c1 = float(input("Digite o valor do cateto oposto: "))
c2 = float(input("Digite o valor do cateto adjacente: "))

h = (c1 ** 2 + c2 ** 2) ** (1/2)


print("O valor da hipotenusa é: {}".format(h))