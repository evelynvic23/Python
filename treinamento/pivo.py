# o split serve para colocar em array
# o map serve para deixar tudo em int

a, b, c = map(int, input().split())

# colocando os valores dentro de uma lista fica mais fácil
lista = [a, b ,c] 
# o .sort() serve para ordenar a lista no menor para o maior
lista.sort()
# com a posição no meio fica perfeito
print(lista[1])


