# 1. Faça um algoritmo (fluxograma e codifique em Python) que leia 3 valores inteiros e positivos,
# encontre o maior e o menor valor lidos, calcule a média dos números lidos e mostre os resultados

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

vetor = [a,b,c]

lista = sorted(vetor)
lista2 = sorted(vetor)

soma = (lista[0] + lista2[2]) 

div = soma / 2

print("A soma dos valores é: ", soma)

print("A média do menor e do maior valor é: ", div)