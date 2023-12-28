import numpy as np 
import statistics as ss
arr=[1,2,3,3,4,5,6,10]

mean=np.mean(arr)
print("mean=",mean)

mode=ss.mode(arr)
print("mode=",mode)

median=np.median(arr)
print("median=",median)