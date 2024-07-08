import numpy as np

rng = np.random.default_rng(seed=42)
vendas = rng.integers(low= 20, high=200, size=30, endpoint= True)

print(vendas)

vendas_reshaped = np.reshape(vendas, (5,6))

print(vendas_reshaped)

total_vendas_semana = vendas_reshaped.sum(axis=1)
print(total_vendas_semana)

total_media_semana = vendas_reshaped.mean(axis=1)
print(total_media_semana)