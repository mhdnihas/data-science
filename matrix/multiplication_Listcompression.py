matrixA=[[1,3,5],[5,6,7],[8,9,10]]
matrixB=[[2,2,2],[3,3,3],[4,4,4]]
result=[
    [sum(a*b for a,b in zip(A_row,B_coloum))
     for B_coloum in zip(*matrixB)]
    for A_row in matrixA
]
for row in result:
    print(row)