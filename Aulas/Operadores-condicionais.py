print("---------------------")
a = float(input("Entre com o primeiro número: "))
b = float(input("Entre com o segundo número: "))
if a > b:
    print(f"{a} é maior que {b}")
else:
    if b > a:
     print(f"{b} é maior que {a}")
    else:
        print("Os dois números são iguais")
print("---------------------")
c = float(input("Entre com o primeiro número inteiro: "))
if(c // 1 != c):
    print("Este numero não é inteiro")
else:
    d = float(input("Entre com o segundo número inteiro: "))
    if (d // 1 != d):
        print("Este número não é inteiro")
    else:
        if (c % 2 == 0) and (d % 2 == 0):
            print("Os dois números são pares")
        else:
            if (c % 2 == 0) and (d % 2 != 0):
                print ("Apenas o primeiro numero é par")
            else:
                if(c % 2 != 0) and (d % 2 == 0):
                    print("Apenas o segundo numero é par")
                else:
                    print("Nenhum dos números digitados são par")
print("---------------------")

