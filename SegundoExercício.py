listaLida = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1]
listaInvertida = []
for i in range(0, len(listaLida)):
    listaLida = listaLida
    listaInvertida.append(listaLida[len(listaLida)-1])
    listaLida.pop()
print("Inversão:",listaInvertida)