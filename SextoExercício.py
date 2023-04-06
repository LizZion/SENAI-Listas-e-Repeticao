alunos = []
notasTemp = []
contagem = 1
contagem2 = 0
mediaTemp = 0
contagem3 = 1
final = ""
for i in range(0,10):
    if contagem == 1:
        print("Insira a primeira nota:")
        notasTemp.append(float(input()))
        contagem += 1
    if contagem == 2:
        print("Insira a segunda nota:")
        notasTemp.append(float(input()))
        contagem += 1
    if contagem == 3:
        print("Insira a terceira nota:")
        notasTemp.append(float(input()))
        contagem += 1
    if contagem == 4:
        print("Insira a quarta nota:")
        notasTemp.append(float(input()))
        for i in notasTemp:
            mediaTemp = mediaTemp + notasTemp[contagem2]
            contagem2 += 1
        mediaTemp = mediaTemp / 4
        alunos.append(mediaTemp)
        mediaTemp = 0
        notasTemp = []
        contagem2 = 0
        contagem = 1
for i in alunos:
    final = f"{final} Aluno {contagem3} - {str(alunos[contagem3-1])} |"
    contagem3 += 1
print("Médias:", final)