faturamento = 1000
custo = 600

lucro = faturamento - custo
texto = f"O lucro foi de R$ {lucro} e o faturamento foi de R$ {faturamento}"

print (texto)

email = "EMAIL_FALSO@gmail.com"

email = email.lower() # colocar em letra miniscula
email = email.strip() # remover os espaços em branco do inicio e do final da string

print (email)
 # email = email.lower() -> email = "

# tamanho
print (len(email)) # quantidade de caracteres da string

# posição    
posicao = email.find("@") # encontrar a posição do @
print (posicao)

#pedaços do texto
print (email[11:]) # email[11:] -> pegar a partir da posição 11 até o final da string

# trocar um pedaco do texto  
email = email.replace("@", "123") # substituir o @ por 123
print (email)

nome = "joao lira" 
titulo = nome.title() # colocar a primeira letra de cada palavra em maiuscula
print (titulo)

# formatação numerica
faturamento = 1000000
custo = 600000

lucro = faturamento - custo
print (f"O lucro foi de R$ {lucro:,.2f} e o faturamento foi de R$ {faturamento:,.2f}")

# exercicios 

nome = "joao paulo lira"
email = "emailfalsodolira@gmail.com"

# descubra o servidor do email 
# descubra o primeiro nome do usuario   
# criar uma mensagem persoanlizada usando o primeiro nome e dizendo que o email foi cadastrado com sucesso

# Exercicio 1: Descobrir o servidor do email (apenas o nome, não o dominio completo)
posicao_arroba = email.find("@")
posicao_ponto = email.find(".", posicao_arroba)
servidor = email[posicao_arroba+1:posicao_ponto]
print(f"Servidor: {servidor}")

# Exercicio 2: Descobrir o primeiro nome do usuario
primeiro_nome = nome[:nome.find(" ")] # pegar o texto até o primeiro espaço
print(f"Primeiro nome: {primeiro_nome}")

# Exercicio 3: Criar uma mensagem personalizada
mensagem = f"Olá {primeiro_nome}, seu email {email} foi cadastrado com sucesso no servidor {servidor}"
print(f"Mensagem: {mensagem}")
