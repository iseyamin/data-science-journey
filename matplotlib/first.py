import matplotlib.pyplot as plt
import numpy as np


x=np.array([2022,2023,2024,2025,2026])
y=np.array([8.8,5.2,6.8,7.7,8.2])
y2=np.array([7,5,5,4,7])

line_style = dict(
        marker=".",
        ms=20,
        mfc="green",
        mec="red",
        linestyle="solid",
        linewidth=5,
        #color="orange"
        )
plt.plot(x,y, color="#9822bf", **line_style)
plt.plot(x,y2,  **line_style)
plt.show()