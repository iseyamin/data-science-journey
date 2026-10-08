import matplotlib.pyplot as plt
import numpy as np


score = np.random.normal(loc=80, scale=10, size=100)
#loc -> location =80 (most of the number around 80, 80 can be median)
#scale -> standard deviation
#size -> total data size

plt.hist(score, bins=10, color="orange", edgecolor="black") #bines-> total partisions
plt.title("Student count with marks")
plt.xlabel("marks")
plt.ylabel("number of students")
print(len(score))
plt.show()