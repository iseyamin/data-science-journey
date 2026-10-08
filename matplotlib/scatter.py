import matplotlib.pyplot as plt
import numpy as np


x1 = np.array([0, 2,3,2,7,5,6,8,6]) #study hours
y1 = np.array([20,33.4,55,40,63,92,83,67,78]) #score

x2 = np.array([1,5,3,2,6,5,6.5,9,6]) #study hours
y2 = np.array([15,23,75,50.8,63,72,84,67,73]) #score

plt.scatter(x1,y1, color='#b5490b', s=150, label="66-B")
plt.scatter(x2,y2, color='#0bb535', s=150, alpha=0.7, label="66-D")

plt.xticks(x1)

plt.title("Student Score with study hour", color="orange", size=20)

plt.legend() #show label information
plt.show()
