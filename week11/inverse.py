def determine(metrix):
    n=len(metrix)

    if n==2:
        return (metrix[0][0] * metrix[1][1] - metrix[0][1] * metrix[1][0])

    elif n==3:
        return (metrix[0][0]*(metrix[1][1]*metrix[2][2]-metrix[1][2]*metrix[2][1])-metrix[0][1]*(metrix[1][0]*metrix[2][2]-metrix[1][2]*metrix[2][0])+metrix[0][2]*(metrix[1][0]*metrix[2][1]-metrix[1][1]*metrix[2][0]))
    else:
        print("It is difficult to find determine")
def inverse(metrix):
    n=len(metrix)
    detem=determine(metrix)
    if detem==0:
        print("it is singular metrix,so we can not find its inverse")
        return
    cofactor=[[None for j in range(len(metrix))] for  i in range(len(metrix))]

    for i in range(len(metrix)):
        for j in range(len(metrix)):
            cofactor[i][j]=((-1)**(i+j))*determine([[metrix[raw][col] for col in range(n) if col!=j]for raw in range(n) if raw!=i])

    adjoint=[[cofactor[col][raw] for col in range(n)]for raw in range(n)]
    invers=[[(element/detem) for element in raw]for raw in adjoint]
    return  invers


metrix=[[1,2,3],[0,1,0],[1,2,1]]
print("metrix:")
for raw in metrix:
    print(raw)
coafactor=inverse(metrix)
print("\ninverse")
for raw in coafactor:
    print(raw)