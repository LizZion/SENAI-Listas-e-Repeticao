print("Insira a população do país A:")
pop_A = float(input())
print("Insira o crescimento do país A:")
cresc_A = (pop_A * float(input())) / 100
print("Insira a população do país B:")
pop_B = float(input()) 
print("Insira o crescimento do país B:")
cresc_B = (pop_B * float(input())) / 100
anos = 0
while pop_A < pop_B:
    pop_A = pop_A + cresc_A
    pop_B = pop_B + cresc_B
    anos += 1
print(anos)