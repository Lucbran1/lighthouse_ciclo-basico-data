# Arquitetura von Neuman
# Guardar variaveis

nome_aluno = "Josepha" #string
idade_aluno = 25 # int
altura_aluno = 1.75 # float
josepha_esta_aprendendo = True # booleano

print (nome_aluno)

print (f"Olá {nome_aluno}, você tem {idade_aluno} anos e mede {altura_aluno} metros.")


# estrutura de decisão
# uso de if e else

nota = 8.5 #int
media = 7.0 #float

if nota >= media:
    resultado = "Aprovado"
elif nota >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print (f"O aluno {nome_aluno} obteve nota {nota} e esta {resultado}")

#Fucoes repetição
# array

def calcular_bonus (salario):
    return salario * 1.1 

salarios = [5000, 7600, 8200] 

print(calcular_bonus(salarios[0])) # calcular o bonus do primeiro salario

for salario in salarios:
    print (calcular_bonus(salario))

    
# criar um array  

tarefas = ["estudar python", "comprar cafe", "lavar o carro", "ir no cinema"]

tarefas.append("fazer exercicios") # adicionar uma nova tarefa no final do array
print (tarefas)

print (tarefas[0]) # acessar a primeira tarefa
print (tarefas[2]) # acessar a terceira tarefa

tarefas.remove("ir no cinema")


# definir classe ( o modelo)
class carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def acelerar(self, aceleracao):
        self.velocidade += aceleracao

        self.frear(self, frenagem): 
        self.velocidade -= frenagem

    # criar um objeto (uma instancia da classe)
meu_carro = carro("Toyota", "Corolla", 2020, "preto")
carro_de_voces = carro("Ferrari", "Puro Sangue", 2019, "vermelha")

Print (f"Meu carro é um {meu_carro.marca} {meu_carro.modelo} do ano {meu_carro.ano} na cor {meu_carro.cor}")
meu_carro.acelerar(100)
print (f"A velocidade do meu carro é {meu_carro.velocidade} km
       

# API REQUESTS

import requests

pokemon = "charmander"
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

try:
    response = requests.get(url)
dados = response.json()

nome = dados["name"]
tipo = dados["types"][0]["type"]["name"]
imagem = dados["sprites"]["front_default"]

print (nome)
print (tipo)
print (imagem)


except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a requisição: {e}")       


