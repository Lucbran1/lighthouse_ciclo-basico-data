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
# descubra o servidor do email 
# descubra o primeiro nome do usuario 

# exemplos de resolução abaixo
email = "EMAIL_FALSO@gmail.com"
email = email.lower().strip()

# servidor é o texto entre '@' e o primeiro '.' após ele
start = email.find("@") + 1
end = email.find(".", start)
servidor = email[start:end]
print("Servidor do email:", servidor)

# usuário vem antes do '@'; o primeiro nome é a parte antes de qualquer separador
usuario = email[:email.find("@")]
primeiro_nome = usuario.split(".")[0].split("_")[0]
print("Primeiro nome do usuario:", primeiro_nome)