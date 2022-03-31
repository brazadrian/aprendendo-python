print("—•—" * 12, sep=" ") #sep = separador
print("Bem vindo ao jogo da adivinhação!")

numero_secreto = int(input("Digite seu número secreto: ")) #inputs entram como str: aqui, convertendo para int
print(numero_secreto) #saída de dado

print(type(numero_secreto)) #saída com o TIPO de dado
# Lembrar que ele foi convertido para int na linha 4

print("—•—" * numero_secreto, sep=" ") # aqui, a var numero_secreto vai multiplicar a str "-•-"
