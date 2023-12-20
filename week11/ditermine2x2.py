def determine(metrix):
    return (metrix[0][0]*metrix[1][1]-metrix[0][1]*metrix[1][0])


metrix=[[1,2],[5,10]]
result=determine(metrix)
print("\ngiven metrix:")
for raw in metrix:
    print(raw)
print("determines is :",result)
