numTodos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numPares = []
numImpares = []
for i in numTodos:
    if numTodos[i-1]%2:
        numImpares.append(numTodos[i-1])
    else: 
        numPares.append(numTodos[i-1])
print("Números:", numTodos)
print("Ímpares:",numImpares)
print("Pares:",numPares)