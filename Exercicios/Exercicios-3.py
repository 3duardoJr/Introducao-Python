print("----------Exercícios----------")
print("i)")
cont = 1
a = 0
b = 0
while cont < 6:
    a = float(input(f"Digite a {cont}° nota: "))
    b = b + a
    cont += 1
media = b/5
print(f"Sua média entre as notas foi de {media:.2f}")
print("------------------------------")
print("ii)")
m = 1
n = 3
for m in range(1, 11):
    result = n*m
    print(f"{n} x {m} = {result}")
    m += 1
