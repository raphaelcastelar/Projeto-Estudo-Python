vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295)]

valores2019 = [vendas2019 for produto, vendas2019, vendas2020 in vendas_produtos]

print(valores2019)
print(max(valores2019))

lista_vendasproduto2019 = [(produto, vendas2019) for produto, vendas2019, vendas2020 in vendas_produtos]
print(max(lista_vendasproduto2019))