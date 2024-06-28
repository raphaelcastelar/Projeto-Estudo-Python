meta = 10000
vendas = {
    'Joao': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana' : 10300,
    'Alon': 7870,

}

def identificar_vendedores(meta, vendas):
    bateram_meta = []
    for vendedor in vendas:
         if vendas[vendedor] >= meta:
            bateram_meta.append(vendedor)

    perc_bateram_meta = len(bateram_meta) / len(vendas)
    return (perc_bateram_meta, bateram_meta)

print(identificar_vendedores(meta, vendas))

            