import math

print("Operações")
print("\n")
print('A sera igual a 10')
print('B sera igual a 3')
print("\n")
a = 8
b=2
#----------------------------Adição---------------------------
print("A soma sera: ", a+b)
print("\n")

#-----------------------------Subtração--------------------------
print("A subtracção de A por B: ", a-b)
print("\n")
print("A subtracção de B por A: ", b-a)
print("\n")

#--------------------------Multiplicação-----------------------------
print("A multiplicação sera: ", a*b)
print("\n")

#-------------------------Divisão------------------------------
print("A divisão de A por B: ", a/b)
r = a/b
print("\n")
print('Arredondando fica: ', round(r, 3))
print("\n")
print("A divisão de B por A: ", b/a)
print("\n")
print("O resto da divisão de A para B é: ", a%b)
print("\n")
print("O resto da divisão de B para A é: ", b%a)
print("\n")
e = a**b

#------------------------Expoente-------------------------------
print("A elevado a B, será: ", e)
print("\n")

#---------------------------Raiz quadrada----------------------------
print("Raiz quadra de A ao cubo é ",math.sqrt(e))
print("\n")
