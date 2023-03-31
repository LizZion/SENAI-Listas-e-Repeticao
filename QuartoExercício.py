ListaVogais = ['a','e','i','o','u']
ListaLetras = ["b","c","a","e","d","z","y","v","x","k"]
ListaConsoantes = []
consoantes = 0
contador = 0
for i in ListaLetras:
    if not ListaLetras[contador] in ListaVogais:
        consoantes += 1
        ListaConsoantes.append(ListaLetras[contador])
    contador += 1
print("Consoantes:", ListaConsoantes)
print("Quantas consoantes:", consoantes)
