import matplotlib.pyplot as plt
import numpy as np

subject = ["OOp","Algorithm","AI","Data Science","Operating System"]
number = np.array([78, 82, 68, 86, 53])


plt.bar(subject,number, color='#73101c')
plt.title("Subject wise marks",
          color='#1e853a',
          fontsize=20)

plt.xlabel("Subject")
plt.ylabel("marks")
plt.tick_params(axis="both", color='#7f9107')

plt.show()