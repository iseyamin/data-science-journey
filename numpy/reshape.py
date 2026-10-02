import numpy as np
array3=np.array([5,8,9,6,23,12,25,6,19,17])

new_array = array3.reshape(2,5)#for 1d to 2d
#.reshape return view, not copy
print(new_array)

#flatten -> multi d to 1d
#.ravel()-> view
#.flatten-> copy
array =np.array([[2,3,9],[6,88,23]])
new_array2 = array.ravel()
new_array3 = array.flatten()

print(new_array3)
new_array3[2] = 100 #it will not modify the original array
print(new_array3)
print(array)

print("\n\n")

print(new_array2)
new_array2[1] = 100 #it will modify the original array
print(new_array2) 
print(array)

