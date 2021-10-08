print("---------------------")
c = float(input("Entre com o primeiro número inteiro: "))
d = float(input("Entre com o segundo número inteiro: "))
swicth = {
    c // 1 != c or d // 1 != d : print("Erro, Você entrou com algum numero que não é inteiro"),
    c % 2 == 0 and d % 2 == 0 : print("Os dois são pares"),
    c % 2 == 0 and d % 2 != 0 : print("Apenas o primeiro numero é par"),
    c % 2 != 0 and d % 2 == 0 : print("Apenas o segundo número é par"),
    c % 2 != 0 and d % 2 != 0 : print("Nenhum dos números digitados são par")
}
print("---------------------")