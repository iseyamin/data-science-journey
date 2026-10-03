import numpy as np
#insert data -> np.insert(array, index, value, axis=None)

arr1 =np.array([5,8,9,6,23,12,25,6,19,17])
arr2 =np.insert(arr1, 3, 500)
print(arr2)

#insert for 2d array

arr3=np.array([[2,3,4],[3,7,9]])
arr4=np.insert(arr3,1,[4,0],axis=1)#column add at 2nd index position
print(arr4)

#insert into last of the array
arr5 = np.append(arr1, [5,77,88])#add to the last of the array
print(arr5)

#Join array or concatenate
arr6 =np.array([3,5,6,7])
arr7 =np.array([4,9,0,5])
arr8 =np.concatenate((arr7,arr6))
arr9 =np.stack((arr7,arr6),axis=0) #row wise stack
arr10 =np.stack((arr7,arr6),axis=1) #column wise stack

print(arr8)
print(arr9)
print(arr10)

#delete array
arr11 = np.delete(arr10,2,axis=0) 
print(arr11)

#Split array
arr12 = np.split(arr1,5)
print(arr12)