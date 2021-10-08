print("\n")
print("--------------------------")
while True:
    try:
        num = int(input("Digite um valor inteiro: "))
    except:
        print("Valor invalido...")
    else:
        print("Seu valor é", num)
        break
print("---")
while True:
    try:
        n = int(input("Digite um valor inteiro: "))
    except ValueError:
        print("Valor invalido...")
    except KeyboardInterrupt:
        print("Até logo usuario")
        break
    else:
        print("Seu valor é", num)
        break
print("--------------------------")
