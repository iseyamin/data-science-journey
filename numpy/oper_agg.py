import numpy as np

#simple mathematical operations
arrayy=np.array([66,6,8,4,3])
print(arrayy + 5)
print(arrayy // 2)
print(arrayy ** 2)

#common aggregation 
total = np.sum(arrayy)
print(total)

print(np.average(arrayy))#average
print(np.mean(arrayy))#average
print(np.std(arrayy))#standard deviation
print(np.var(arrayy))#varience
print(np.min(arrayy))#minimum