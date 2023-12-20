def multiplication(metrix1,metrix2):
    result=[[0 for i in range(len(metrix1))] for j in range(len(metrix2[0]))]
    for i in  range(len(metrix1)):
        for j in range(len(metrix2[0])):
            sum=0
            for k in range(len(metrix1[0])):
                sum+=metrix1[i][k]*metrix2[k][j]
            result[i][j]=sum
    return result
def display(metrix):
    for raw in metrix:
        print(raw)
metrix1=[[1,2,3],[2,1,2],[1,1,1]]
metrix2=[[1,2,1],[1,1,1],[3,3,3]]
result=multiplication(metrix1,metrix2)
print("\nMETRIX MULTIPLICATION\n")
print("First metrix:")
display(metrix1)
print("second metrix:")
display(metrix2)
print("result:")
display(result)
