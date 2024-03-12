import Pylance

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul','ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_ano = vendas_1sem + vendas_2sem

maior_venda = max(vendas_ano)
menor_venda = min(vendas_ano)

indice_maior_valor = vendas_ano.index(maior_venda)
indice_menor_valor = vendas_ano.index(menor_venda)



print(f"O melhor mês do ano foi {meses[indice_maior_valor]} com {maior_venda} vendas")
print(f"O pior mês do ano foi {meses[indice_menor_valor]} com {menor_venda} vendas")

