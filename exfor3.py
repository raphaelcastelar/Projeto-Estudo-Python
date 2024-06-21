meta = 10000
vendas  = [
['João,', 9000],
['Julia', 21700],
['Marcus', 9900],
['Maria', 3750],
['Ana', 10000],
['Alon', 7870],
]

acima_meta = []
for venda in vendas:
    if venda[1] >= meta:
        acima_meta.append(venda)
        
       
print('{:%} dos vendedores bateram a meta'.format(len(acima_meta) / len(vendas)))

print(acima_meta)
maiorvenda = 0
for vendeumais in acima_meta:
    if vendeumais[1] > maiorvenda:
        maiorvenda = vendeumais[1]
        melhor_vend = vendeumais[0]
print(maiorvenda, melhor_vend)


