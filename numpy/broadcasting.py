#without numpy
p=[100,200,300,400]
d=10
np=[]
for i in p:
    n=i-(i*d/100)
    np.append(n)
print(np)

#with numpy
import numpy as np

prices = np.array([100,200,300,400,500,600,700])
discount = 10
new_price=prices-(prices*discount/100)
print(new_price)

#mathematical operations between 2 array-> they should be same size or one single value
#[1,2,3]+10 = correct
#[1,2,3]+[4,5,6]=correct
#[1,2,3]+[4,5]+error
arr =np.array([10,20,30])
arr1 =np.array([[1,2,3],[4,5,6]]) #(2x3)
arr2 =np.array([[2,3,4,1],[1,1,1,1],[2,2,2,2]]) #(3x4)
arr3 = arr + arr1
print(arr3)