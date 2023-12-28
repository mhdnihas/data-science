#mean
def mean(list):
    sum=0
    for i in list:
        sum+=i
    return sum/len(list)

#median
def median(list):
    n=len(list)
    if n%2==0:
        median=(list[n//2]+list[n//2-1])/2
    else:
        median=list[n//2]
    return median

#mode
def mode(list):
    dic={}
    for num in list:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    mode=[num for num,count in dic.items() if max(dic.values())==count]
    return mode

list=[1,2,3,4,4,5,5,5,6,6,6,7]

print("mean=",mean(list))
print("median=",median(list))
print("mode=",mode(list))