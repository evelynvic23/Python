
# Evelyn Victoria | 24/04/2024

contatos = []


while True:


    d = input("Digite s para sair ou n para continuar: ")
  
    if d.lower() == 's':
        break

    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")

    
  
    contato = {'Nome': nome, 'Telefone': telefone, 'E-mail': email}
    
  
    contatos.append(contato)


print("\nContatos cadastrados:")
for contato in contatos:
    print("Nome:", contato['Nome'])
    print("Telefone:", contato['Telefone'])
    print("E-mail:", contato['E-mail'])
    print()
