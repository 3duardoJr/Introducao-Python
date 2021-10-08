print("\n")
print("-----------------")
lista = [1, 1]
cont = 1
pos = 0

while cont <= 2:
    try:
        lista[pos] = (float(input(f'Digite o {cont}° valor: ')))
        divisao = lista[0] / lista[1]
        soma = lista[0] + lista[1]
        cont += 1
        pos += 1
    except ValueError:
        print("Por favor, digite um número")
    except ZeroDivisionError:
        print("0(zero) não é divisivel")
    except KeyboardInterrupt:
        print("Programa interrompido")
print("---")
print(f"O resultado da divisao entre eles é: {divisao}")
print(f"A soma dos itens da lista é: {soma}")
print("-----------------")
