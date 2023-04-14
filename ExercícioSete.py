numeros = [3,5,8,2,4]
tempNumber = 0
for i in range(len(numeros)):
    if numeros[i] > tempNumber:
        tempNumber = numeros[i]
print(tempNumber)