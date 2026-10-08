import matplotlib.pyplot as plt
import numpy as np

subject = ["OOp","Algorithm","AI","Data Science","Operating System"]
number = np.array([78, 82, 68, 86, 53])

colorss = ['#5a88d1','#38965a','#9a2bb3','#b33d2b','#ccb90e']
myexplode = [0.2, 0, 0, 0,0]


plt.pie(number, labels=subject, autopct="%1.1f%%", explode=myexplode, 
        colors=colorss)
plt.title("Subject wise marks",
          color='#1e853a',
          fontsize=20)

plt.legend() #showing details of color identifier

# plt.xlabel("Subject")
# plt.ylabel("marks")
# plt.tick_params(axis="both", color='#7f9107')

plt.show()