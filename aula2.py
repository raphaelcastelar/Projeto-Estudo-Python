
produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'maquina de café', 'kindle']

produtos_ecommerce = [[10000, 2500],
                     [50000, 40],
                     [7000, 1200],
                     [20000, 1500],
                     [5800, 1300],
                     [7200, 2500],
                     [200,800],
                     [3300, 700],
                     [1900,400]]

reajuste_livro = produtos_ecommerce[1][1] * 0.1
produtos_ecommerce[1][1] = produtos_ecommerce[1][1] + reajuste_livro
print(produtos_ecommerce)
print(f"O aumento do custo mensal vai ser em média {(produtos_ecommerce[1][1] * 0.1) * produtos_ecommerce[1][0]}")
