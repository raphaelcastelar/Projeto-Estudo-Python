import numpy as np

rng = np.random.default_rng(seed=42)
vendas = rng.integers(low= 20, high=200, size=30, endpoint= True)



vendas_reshaped = np.reshape(vendas, (5,6))



total_vendas_semana = vendas_reshaped.sum(axis=1)
print(total_vendas_semana)