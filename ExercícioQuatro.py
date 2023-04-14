pop_A = 80000
cresc_A = (pop_A * 3) / 100
pop_B = 200000 
cresc_B = (pop_B * 1.5) / 100
anos = 0
while pop_A < pop_B:
    pop_A = pop_A + cresc_A
    pop_B = pop_B + cresc_B
    anos += 1
print(anos)