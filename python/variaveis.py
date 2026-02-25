faturamento = 1000 # int
custo = 600

novas_vendas = 1100
faturamento = faturamento + novas_vendas

imposto = 0.15 * faturamento # float   
print (imposto)

lucro = faturamento - custo - imposto



print ("faturamento", faturamento)
print ("custo", custo)
print ("lucro", lucro)


messagem = "O faturamento da loja foi de R$ 2100" # string
teve_lucro = True #boolean

margem_lucro = lucro / faturamento * 100
print ("margem", margem_lucro)


# int = numeros inteiros
# float = numeros decimais
# strings  = texto
# boleanos = verdadeiro ou falso    

# operadores especiais

# mod -> %
# resto da divisão de um numero por outro
# 10 % 3 

anos = int (310/12) # 25
print (anos, "anos")

meses = 310 % 12 # 10
print (meses, "meses")



# floor division -> //