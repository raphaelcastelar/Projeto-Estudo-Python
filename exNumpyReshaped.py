import numpy as np

vendas = np.array([ 200, 220, 250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220])

vendas_reshaped = np.reshape(vendas, (2,7))

print(vendas_reshaped)