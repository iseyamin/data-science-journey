import numpy as np


#Indexing
array =np.array([[2,3,9],[6,88,23]])
print(array[1,2])#second row and third column

array2=np.array([4,67,82,39,56])
print(array2[-2])#second last element


#Slicing
array3=np.array([5,8,9,6,23,12,25,6,19,17])
slicearray=array3[1:5:1]#[start:stop:step]
print(slicearray)
print(array3[3:6])#4th element to 6th element
print(array3[:6])#first element to 6th
print(array3[3:])#4th element to last
print(array3[::2])#skip one element 
print(array3[::-1])#reverse array

#fancy indexing -> find multiple index at a time
print(array3[[2,4,6]])#3rd, 5th and 7th element