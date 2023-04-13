vetor_A = []
vetor_B = []
for i in range(10):
    num_A = int(input(f"Digite o {i+1}º elemento do vetor A:"))
    vetor_A.append(num_A)
    num_B = int(input(f"Digite o {i+1}º elemento do vetor B:"))
    vetor_B.append(num_B)

intercalado = []
for i in range(10):
    intercalado.append(vetor_A[i])
    intercalado.append(vetor_B[i])

print("Vetor A:", vetor_A)
print("Vetor B:", vetor_B)
print("Intercalada:", intercalado)
