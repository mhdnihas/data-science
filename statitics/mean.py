import numpy as np 
from scipy import stats
arr=[1,2,3,3,4,5,6,10]
mean=np.mean(arr)
print("mean=",mean)
mode=stats.mode(arr)
print(mode)
median=np.median(arr)
print("median=",median)