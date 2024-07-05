import numpy as np


rng = np.random.default_rng()

dados = rng.integers(low = 50, high = 200, size = 30)
print(dados)

print(rng)

inter = rng.integers(low=22, high = 30, size= 2 )