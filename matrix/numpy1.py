import numpy as np
print("hei")

num=[1,2,3,4]
a=np.array(num)
print(a)

vector=np.array([1,2])
metrix=np.array([[10,10],[20,5]])
result=np.dot(vector,metrix)
print(result)
print(np.eye(4))

print(np.diag(num))
print(np.arange(0,9).reshape(3,3))
l=[12.443,25.6,4.5,5.6]
a=np.array(l)
print(a)

x=np.random.random((5,5))
print(x)
xmin,xmax=x.min(),x.max()
print(xmin,xmax)
num1=np.arange(1,7).reshape(3,2)
print(num1)
print(np.trace(num1))