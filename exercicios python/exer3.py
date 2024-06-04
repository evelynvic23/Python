# Faça um algoritmo (fluxograma e codifique em Python) auxiliar no controle de 
# qualidade de uma fábrica de pisos, imprimindo os números das peças reprovadas, 
# bem como o total de peças aprovadas e reprovadas no final do dia. Considere que a 
# fábrica tem uma linha de produção 
# capaz de produzir 800 peças por dia e para controlar a qualidade deve-se 
# cadastrar o número da peça e o seu estado (aprovado ou reprovado).

aprovadas = 0
reprovadas = 0

while aprovadas + reprovadas <= 800:
    numero = int(input("Digite o número da peça: "))
    estado = input("Digite aprovado ou reprovado: ")
    
    
    if estado.lower() == "aprovado":
        aprovadas += 1
    else:
        reprovadas += 1
        print("Número da peça reprovada: ", numero)
        
    # Para sair do laço de repetição
        
    sair = input("Digite 's' para sair ou 'n' para continuar: ")
        
    if sair.lower() == "s":
        print("\nProcesso encerrado pelo usuário.")
        break
    
print("\nTotal de peças aprovadas:", aprovadas)
print("Total de peças reprovadas:", reprovadas)
    
