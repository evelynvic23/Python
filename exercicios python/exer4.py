# Faça um algoritmo para calcular a conta final de um hóspede de uma certa pousada. 
# Essa conta deve conter o nome do hóspede, o tipo do 
# apartamento, o número de diárias usadas, o valor unitário da diária, o valor total das diárias, 
# o valor do consumo interno, o subtotal, o valor da taxa de serviço e o total geral.

nome = input("Digite o nome do hóspede: ")
apartamento = input("Digite o tipo de apartamento: A, B, C, D: ")
diarias = int(input("Digite o número de diárias usadas: "))

if apartamento.upper() == "A":
    valor_diaria = 250.00
elif apartamento.upper == "B":
    valor_diaria = 150.00
elif apartamento.upper == "C":
    valor_diaria = 100.00
elif apartamento.upper == "D":
    valor_diaria = 75.00
else:
    print("Apartamento não encontrado!")
    

total_diarias = diarias * valor_diaria

consumo = float(input("Digite o consumo interno: "))

subtotal = total_diarias + consumo

taxa = subtotal * 0.10

total = subtotal + taxa

print("\n--- Conta Final ---")
print("Nome do hóspede:", nome)
print("Tipo do apartamento:", apartamento.upper())
print("Número de diárias usadas:", diarias)
print("Valor total das diárias: R$", total_diarias)
print("Valor do consumo interno: R$", consumo)
print("Subtotal: R$", subtotal)
print("Valor da taxa de serviço: R$", taxa)
print("Total geral: R$", total)