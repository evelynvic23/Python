# Evelyn Victoria da Silva Santos

print("Exemplificando estrutura paecida com switch case")

dia = int (input("Informe um dia da semana (Em número): " ))

match dia:
    case 1: print("Domingo")
    case 2: print("Segunda")
    case 3: print("Terça")
    case 4: print("Quarta")
    case 5: print("Quinta")
    case 6: print("Sexta")
    case 7: print("Sábado")
    # caso contrário _
    case _: print("Valor inválido")


s = 0 # Variável acumuladora
print("Imprimindo a soma dos números informados")
while True:
    v = int(input("Entre um número a somar ou 0 para sair: "))
    if v == 0:
        break
    s = v+s #acumulando valor
print ("=====================================")
print("A soma dos números digitados é igual a = ", s)
print("Fim do programa")


p = 0
i = 1

q = int(input("Digite um número: "))
print("Imprimindo números pares: ")
while i <= q:
    print(p)
    i = i+1
    p = p+2
print("Fim do programa")




soma = 0

for i in range (1, 3, 1):

    nome = str(input("Digite o nome do aluno: "))


    p1 = float(input("Digite a primeira nota: "))
    p2 = float(input("Digite a segunda nota: "))

    m = (p1 + p2)/2

    soma = soma + m

    print("O aluno: ", nome)
    print("A média das notas é: ", m)

mturma = soma / 3

print("Média da turma: ", mturma)

