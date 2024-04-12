# Evelyn Victoria 2024 

num1 = int(input("Digite um número entre 1 e 10: "))

print("Tente acertar o número digitado pelo primero jogador!")

num2 = int(input("Digite um número entre 1 e 10: "))

if num1 < 1 or num1 > 10:
    print("Por favor, digite um número entre 1 e 10!")
elif num2 < 1 or num2 > 10:
    print("Por favor, digite um número entre 1 e 10!")

else:
    tentativas = 1 
    
    while num1 != num2:
        tentativas += 1  
        
     
        opcao = input(str("Errou! Quer tentar novamente? (escolha sim/nao): "))
        
     
        if opcao == "sim":
            num2 = int(input("Digite um número entre 1 e 10: "))
  
        elif opcao == "nao":
            print("Obrigado por participar!")
            break
        else:
            print("Opção inválida! Por favor, escolha 'sim' ou 'nao'.")


    if num1 == num2:
        print("Parabéns! Você acertou o número em", tentativas, "tentativa(s).")
