carros = ['Ferrari', 'Civic', 'Touro']

# Imprimindo elementos de um vetor

print(carros[1], carros[2])

# Para acessar o último elemento -1

# ////////////////////////////////////////////////

# Manipulando elementos de uma lista

# Trocando elemento

carros[1] = 'Mustang'
print(carros[1])

carros[2] = 'BMW'
print(carros)

# A função append() adiciona novos elementos no final da lsita
carros.append('Civic')

print(carros)

# Com o método insert é possível escolher a posição na lista

carros.insert(1, 'jeep')

print(carros)

# A função extend adiciona elementos porém cada caractere é reconhecido como elemento

carros.extend('uno')

print(carros)

# O método del é usado para remover elementos

del carros[1]
print(carros)

# Remove é utilizado com o nome próprio

carros.remove('u')
carros.remove('n')
carros.remove('o')

print(carros)


# ////////////////////////////////////////////////////////////////////

# Organizando listas

carros.sort() # ordem alfabética

carros.sort(reverse = True) # ordem alfabética inversa

print(carros)

print(sorted(carros)) # somente para o print


# Tamanho da lista
print(len(carros))

# Trocar ordem

frutas = ['morango', 'uva']
print(frutas)

frutas.reverse()

print(frutas)





  