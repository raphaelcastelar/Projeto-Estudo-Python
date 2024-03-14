qtde_pessoas = int(input("Quantas pessoas terão no quarto? "))
quarto = []

for i in range(qtde_pessoas):
    quarto.append(input("Qual o Seu nome? "))
    quarto.append(input("Qual o CPF? "))

print(quarto)
