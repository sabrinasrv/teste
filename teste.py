# Inicializando o contador de respostas positivas
respostas_positivas = 0

# Fazendo as perguntas
resposta_a = input("Telefonou para a vítima? (sim ou não): ").lower()
resposta_b = input("Esteve no local do crime? (sim ou não): ").lower()
resposta_c = input("Mora perto da vítima? (sim ou não): ").lower()
resposta_d = input("Devia para a vítima? (sim ou não): ").lower()
resposta_e = input("Já trabalhou com a vítima? (sim ou não): ").lower()

# Verificando respostas positivas e atualizando o contador
if resposta_a == "sim":
    respostas_positivas += 1
if resposta_b == "sim":
    respostas_positivas += 1
if resposta_c == "sim":
    respostas_positivas += 1
if resposta_d == "sim":
    respostas_positivas += 1
if resposta_e == "sim":
    respostas_positivas += 1

# Emitindo a classificação de acordo com as respostas positivas
if respostas_positivas == 2:
    print("Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
    