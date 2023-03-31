notas = [7.5,5.5,10,9.5]
média = 0
for i in range(0, len(notas)):
    print("Nota", i+1,":", notas[i])
    média = média + notas[i]
média = média / len(notas)
print("Média:",média)