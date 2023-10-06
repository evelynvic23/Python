# Importando o módulo/dependência do twilio

from twilio.rest import Client

# Sua conta

account_sid = "ACc1355f99fb4366e1e6445a3504d8cb17"

# Seu Token

auth_token = "5bc54d298d93f16e2c0f9fac06c4d9fd"


# Criar variável de autenticação de usuário e senha (SID e TOKEN)

envio = Client(account_sid, auth_token)

# Fazer o envio

envio.messages.create(from_="+1 248 876 3607", body="Bem Vindo ao Senai! Evelyn Victoria", to="+5511977265580")
