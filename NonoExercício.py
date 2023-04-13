vetor_A = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro:"))
    vetor_A.append(num)

soma_quadrados = sum([num**2 for num in vetor_A])

print("Vetor A:", vetor_A)
print("Soma dos quadrados:", soma_quadrados)