import numpy as np

#Shape check(one d, two d, how many rows, columns)
#Size= how many elements on the array

array1=np.array([[3,7,66,6],[4,33,23,45]])
print(array1.shape)#(2,4)
print(array1.size)#8

#Dimension -> name.ndim 

array2=np.array([66,6,88,4,3])
array3=np.array([[[3,5,6],[4,7,9],[6,9,0],[6,55,44]]])
print("array3: ",array3.ndim,"D array.",end="")#3
print(" array1: ",array1.ndim,"D array.",end="")#2
print(" array2: ",array2.ndim,"D array.")#1
print(array3.shape)#(1,2,4)

print(array2.dtype)#data type of array
#change data type
array4 =array2.astype(float)
print(array4)
print(array4.dtype)