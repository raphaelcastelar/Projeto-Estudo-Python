preco = 1500
custo = 400
lucro = 800

def calcular_imposto(preco, custo, lucro):
    valor_tributo = preco - custo - lucro
    porcentagem_imposto = valor_tributo / preco
    return porcentagem_imposto

print('A carga tributária foi de {:.1%}'.format(calcular_imposto(preco, custo, lucro)))
    

