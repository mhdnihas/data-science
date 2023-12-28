from math import sqrt
#covarience
def covarience(x,y):
    size=len(x)
    xmean=sum(x)/size
    ymean=sum(y)/size
    sums=sum((x[i]-xmean)*(y[i]-ymean) for i in range(size))
    covarience=sums/size
    return covarience

#correlation
def correlation(x,y):
    size=len(x)
    cov=covarience(x,y)
    meanx=sum(x)/size
    meany=sum(y)/size
    stdv_x=sqrt(sum((x[i]-meanx)**2 for i in range(size))/size)
    stdv_y=sqrt(sum((y[i]-meany)**2 for i in range(size))/size)
    
    r=cov/(stdv_x*stdv_y)
    return r
    
    
list1=[1,2,3,4,5]
list2=[2,4,6,8,10]
print("covarience=",covarience(list1,list2))    
print("correlation=",correlation(list1,list2))