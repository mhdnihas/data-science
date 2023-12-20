matrixA=[[1,3,5],[5,6,7],[8,9,10]]
matrixB=[[2,2,2],[3,3,3],[4,4,4]]
result=[[matrixA[i][j]+matrixB[i][j] for j in range(len(matrixA[0]))] for i in range(len(matrixA))]
print("Addition:")
for row in result:
    print(row)

