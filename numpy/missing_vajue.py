import numpy as np

arr =np.array([2, 44,np.nan , 43, 7, np.nan ])  #np.nan -> no data
print(np.isnan(arr))

#fill all nan data into same value
clean_arr =np.nan_to_num(arr, nan=100) 
print(clean_arr)