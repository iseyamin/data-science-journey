import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x1 = np.array([0, 2,3,2,7,5,6,8,6]) #study hours
y1 = np.array([20,33.4,55,40,63,92,83,67,78]) #score

x2 = np.array([1,5,3,2,6,5,6.5,9,6]) #study hours
y2 = np.array([15,23,75,50.8,63,72,84,67,73]) #score


subject = ["OOp","Algorithm","AI","Data Science","Operating System"]    #for bar
number = np.array([78, 82, 68, 86, 53])

score = np.array([44,60,77,86,68,74,66,94,65,87,49,65,59,73,75,77,80,78,59,73,56,66]) #for histogram

colorss = ['#5a88d1','#38965a','#9a2bb3','#b33d2b','#ccb90e'] #for pie


figure, ax = plt.subplots(2, 2)

ax[0,0].scatter(x1,y1, color='#b5490b', s=150, label="66-B")
ax[0,0].scatter(x2,y2, color='#0bb535', s=150, alpha=0.7, label="66-D")

ax[0,1].bar(subject,number, color='#73101c')

ax[1,0].hist(score, bins=6,  color="orange", edgecolor="black")

ax[1,1].pie(number, labels=subject, autopct="%1.1f%%", colors=colorss)

plt.show()