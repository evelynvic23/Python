# Enunciado para o fluxograma: Teorema de Pitágoras
# Com repetição
# Aqui eu abro um while para que enquanto a resposta do usuário for sim, o código roda

while True:
    c1 = float(input("Digite o valor do cateto oposto: "))
    c2 = float(input("Digite o valor do cateto adjacente: "))

    h = (c1 ** 2 + c2 ** 2) ** (1/2)

    print("O valor da hipotenusa é: {}".format(h))

    continuar = input("Deseja calcular outra hipotenusa? (s/n): ")
    if continuar.lower() != 's':
        break