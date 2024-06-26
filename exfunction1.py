def ealcoolico(bebida):
    bebida = bebida.lower()
    if 'beb' in bebida:
        return True
    

produtos = ['beb46275', 'TFA23962']


for produto in produtos:
    if ealcoolico(produto):
        print("Enviar o produto {} para o setor de bebidas alcoolicas".format(produto))


