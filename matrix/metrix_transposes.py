def transpose(metrix):
    result=[[0 for colomn in range(len(metrix[0]))] for row in range(len(metrix)) ]
    for i in range(len(metrix)):
        for j in range(len(metrix[0])):
            result[i][j]=metrix[j][i]
    return  result

metrix=[[1,2,3],[4,5,6],[7,8,9]]
result=transpose(metrix)

print("matrix:")
for raw in metrix:
    print(raw)

print("transpose of metrix:")
for raw in result:
    print(raw)

