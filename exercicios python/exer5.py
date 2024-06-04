# imposto de renda

while True:

    nome = input("Digite o nome do contribuinte: ")
    cpf = int(input("Digite o CPF do contribuinte: "))
    renda_anual = float(input("Digite a renda anual: "))
    dependentes = int(input("Digite o número de dependentes: "))

    renda_liquida = renda_anual - (dependentes * 200)

    # Verifica a alíquota de imposto de renda com base na renda líquida
    if renda_liquida <= 1903.98:
        ali = 0
    elif renda_liquida <= 2826.65:
        ali = 7.5
    elif renda_liquida <= 3751.05:
        ali = 15
    elif renda_liquida <= 4664.68:
        ali = 22.5
    else:
        ali = 27.5

    # Calcula o valor do imposto de renda
    imposto = (renda_liquida * ali) / 100
    
    print()

    print("_____________Resultados______________")
    print("Nome do contribuinte: ", nome)
    print("CPF do contribuinte: ", cpf)
    print("Renda líquida anual: R$", renda_liquida)
    print("Alíquota de imposto de renda:", ali, "%")
    print("Imposto de renda a pagar: R$", imposto)

    print()
    
    continuar = input("Deseja realizar a declaração de outro contribuinte: sim ou nao: ")
    if continuar.lower() != 'sim':
            break



    
   
        
        