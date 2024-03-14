qtde_pessoas = int(input("Quantas pessoas terão no quarto? "))
quarto = []

for i in range(qtde_pessoas):
  
    nome = input("Qual o nome: ")
    cpf = input("Qual o CPF: ")
    hospede = [nome, "CPF: " + cpf]
    quarto.append(hospede)


print(quarto)
