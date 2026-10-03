import numpy as np

arr1 =np.array([[1,2,3],[4,5,6]]) #(2x3)
arr2 =np.array([[2,3,4,1],[1,1,1,1],[2,2,2,2]]) #(3x4)
arr3 = np.dot(arr1,arr2) #matrix multiplication
print(arr3)