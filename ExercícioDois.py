print("Insira um nome de usuário:")
user = input()
print("Insira uma senha:")
password = input()
while user == password:
    print("Insira uma senha diferente do seu nome de usuário!")
    password = input()