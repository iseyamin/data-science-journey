#Create of array from list
import numpy as np

temperature = np.array([30.5,5.4,22,21,34,40.6,21])
average = np.mean(temperature)
print(average)

#Create 2d of array from list , one kind of matrix
array2 = np.array([[1,4,55],
                  [4,66,54],[44,66,77]])
print(array2)
print(type(array2))

#default array
#zeros array -> np.zeros
zeros_array =np.zeros(5)
print(zeros_array)
#ones array ->np.ones
ones_array =np.ones((3,5))
print(ones_array)
#for pass any random value, use full array-> np.full(  ,random number)
random_array =np.full(2,3)
print(random_array)
random2d_array =np.full((4,3),11)
print(random2d_array)
#declare identy matrix-> np.eye
i_matrix =np.eye(6)
print(i_matrix)
