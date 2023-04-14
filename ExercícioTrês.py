sexos = ["m","f"]
estados_civis = ["s","c","v","d"]
print("Insira seu nome:")
nome = input()
while len(nome) <= 3:
    print("Seu nome tem que ter mais de três letras!")
    nome = input()
print("Insira sua idade:")
idade = int(input())
while  idade < 0 or idade > 150:
    print("Sua idade tem que ser entre 0 a 150!")
    idade = int(input())
print("Insira sua renda:")
renda = float(input())
while renda <= 0:
    print("Sua idade tem que ser maior que 0!")
    renda = float(input())
print("Insira seu gênero (m,f):")
sexo = str(input())
while not sexo in sexos:
    print("Escolha um gênero entre 'm' e 'f'!")
    sexo = str(input())
print("Insira seu estado civil (s,c,v,d):")
estado_civil = str(input())
while not estado_civil in estados_civis:
    print("Escolha um estado civil entre 's','c','v','d'!")
    estado_civil = str(input())