i = int(input("Entre com sua idade: "))
if i < 0:
    print("Idade invalida")
elif i >= 0 or i <= 12:
    print("É uma criança")
elif i >= 13 or i <= 17:
    print("É um adolescente")
elif i >= 18:
    print("É um adulto")
else:
    print("Idade invalida")
