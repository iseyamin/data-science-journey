import matplotlib.pyplot as plt
import numpy as np


score = np.array([44,60,77,86,68,74,66,94,65,87,49,65,59,73,75,77,80,78,59,73,56,66])

plt.hist(score, bins=6)

plt.show()