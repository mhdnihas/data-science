import numpy as np
x=[1,2,3,4,5]
y=[2,3,4,5,6]
print("covariance: ",np.cov(x,y)[0,0])
print("correlation: ",np.corrcoef(x,y))
