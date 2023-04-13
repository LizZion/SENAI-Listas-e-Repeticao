aluno1 = [4,4,10,10]
aluno2 = [9,8,7,6]
aluno3 = [4,5,6,7]
aluno4 = [7.5,9,5,8]
aluno5 = [2,2,2,1]
aluno6 = [6,8,7,7]
aluno7 = [7,8,4,9]
aluno8 = [10,10,10,10]
aluno9 = [5,5,7,7]
aluno10 = [5,6,4,3]
alunos = [aluno1,aluno2,aluno3,aluno4,aluno5,aluno6,aluno7,aluno8,aluno9,aluno10]
contagem = 1
contagem2 = 0
final = ""
media = 0
for i in alunos:
    for nota in alunos[contagem2]:
        media = media + nota 
    media = media / len(alunos[contagem2])
    if media >= 7:
            final = f"{final} Aluno {contagem2+1} (Aprovado) - {media} |"
    contagem2 += 1
    media = 0
print("Médias:", final)