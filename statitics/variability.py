from math import sqrt

#varience
def variance(list):
    n=len(list)
    mean=sum(list)/n
    add=0
    for num in list:
        diff=num-mean
        add+=diff**2
    variance=add/n
    return variance

#standered deviation
def standerd_deviation(list):
    var=variance(list)
    stdv=sqrt(var)
    return stdv

#range
def range(list):
    maximum=max(list)
    minimum=min(list)
    range=maximum-minimum
    return range


list=[1,2,3,4,5]
print("\tMessure of Variability\n")
print(list)
print("vairence=",variance(list))
print("standered deviation=",standerd_deviation(list))
print("range=",range(list))
    