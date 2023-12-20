def determine(metrix):

    return (metrix[0][0]*(metrix[1][1]*metrix[2][2]-metrix[1][2]*metrix[2][1])-metrix[0][1]*(metrix[1][0]*metrix[2][2]-metrix[1][2]*metrix[2][0])+metrix[0][2]*(metrix[1][0]*metrix[2][1]-metrix[1][1]*metrix[2][0]))

print("\nDETERMINES OF METRIX 3X3")
metrix=[[1,2,3],[0,1,0],[1,2,1]]
print("\nMetrix:")
for raw in metrix:
    print(raw)
result=determine(metrix)
print("\ndetermine is :",result)
