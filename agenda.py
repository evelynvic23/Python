nomes = []
telefones = []
emails = []
print("\n\n ============ Cadastro de Contatos ============")
while True:
    nome = input("Informe o NOME do seu contato: ")
    if nome == "0":
       break
    nomes.append(nome)
    telefones.append(input("Informe o TELEFONE do seu contato: "))
    emails.append(input("Informe o EMAIL do seu contato: "))

print("\n\n ============ Pesquisando Contato Cadastrado =============")
buscaNome = input("\ninforme o nome para pesquisar: ")
achou = False
for i in range (len(nomes)):
    if nomes[i] == buscaNome:
        print(nomes[i])
        print(telefones[i])
        print(emails[i])
        flag = True 
        break
else:
    print("Contato não localizado!")


