numeros = [3,5,8,2,4]
Media = 0
tempSoma = 0
for i in range(len(numeros)):
    tempSoma += numeros[i]
Media = tempSoma / len(numeros)
print("Soma:",tempSoma)
print("Média:",Media)