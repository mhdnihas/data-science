import numpy as np
rolls=np.random.randint(1,7,10)
print(rolls)
count=0
one=[1 for i in rolls if i==1]
print(sum(one)/10)