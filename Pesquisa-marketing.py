# Pesquisa com 10 entrevistados

ruim = 0
excelente = 0

# Contador de opiniões

for i in range(50):
    nome = input("Escreva qual é o seu nome:")
    idade = input("Quantos anos você tem? Digite aqui:")
    valor = print("Considerando que:"), print("1:Excelente, 2:Bom, 3:Ruim") ; 
    opiniao = input("Qual nota você dá para o atendimento? Digite aqui:") 
    match opiniao:
        case "1":
            excelente +=1
        case "3":
            ruim +=1

# Total de opiniões
print("O total de pessoas que selecionaram excelente foi:", excelente, )
print("O total de pessoas que selecionaram ruim foi:", ruim,)