matrixA=[[1,3,5],[5,6,7],[8,9,10]]
matrixB=[[2,2,2],[3,3,3],[4,4,4]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrixA)):
    for j in range(len(matrixA[0])):
        result[i][j]=matrixA[i][j]+matrixB[i][j]

print("\nAddition:\n")
print("First Metrix:")
for raw in matrixA:
    print(raw)
print("\nsecond Metrix:")
for raw in matrixB:
    print(raw)
print("\nAfter Addition:")
for row in result:
    print(row)

