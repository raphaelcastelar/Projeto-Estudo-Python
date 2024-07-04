import numpy as np

dados = [ 127, 90, 201, 150, 210, 220, 115]

vendas = np.array(dados)
media = np.mean(vendas)
print(media)

precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])
preco_maximo = np.max(precos)
preco_minimo = np.min(precos)
variacao_preco = preco_maximo - preco_minimo
print("O preço máximo foi de {}, o mínimo foi de {}, e a variação foi de {}".format(preco_maximo,preco_minimo,variacao_preco))