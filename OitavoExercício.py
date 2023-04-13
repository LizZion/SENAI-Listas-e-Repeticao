idades = []
tempVar = []
resultado = ""
for i in range(0,5):
    print("Insira a idade:")
    tempVar = input()
    print("Insira a altura:")
    tempVar = [tempVar, input()]
    idades.append(tempVar)
    tempVar = []
contador = len(idades)
for i in range(0,contador):
    resultado = f"{resultado} {idades[contador-1]}"
    contador -= 1
print(resultado)