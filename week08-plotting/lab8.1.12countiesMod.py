import numpy as np
import matplotlib.pyplot as plt

possibleCounties = ['Mayo', 'Tyrone', 'Cork', 'Donegal', 'Clare']
counties = np.random.choice(possibleCounties, p = [0.1, 0.3, 0.2, 0.12, 0.28], size = (100))

unique, counts = np.unique(counties, return_counts = True)
plt.bar(unique, counts)
plt.show()