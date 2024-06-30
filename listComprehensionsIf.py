meta = 1000
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

produtos_bateram_meta = []

for i, produto in enumerate(produtos):
    if vendas_produtos[i] >= meta:
        produtos_bateram_meta.append(produto)

print(produtos_bateram_meta)

list_aux = zip(vendas_produtos, produtos)
list_compre =  [produtos1 for vendas, produtos1 in list_aux if vendas >= meta]
print(list_compre)

produto_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] >= meta]
print(produto_acima_meta)