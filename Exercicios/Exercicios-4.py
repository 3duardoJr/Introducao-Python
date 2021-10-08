import numpy as np
print("\n")
print('#--------------------Exercícios-------------------#')
print("i)")
cont = 0
pos = 1
l1 = []
while cont < 5:
    n = float(input(f"Digite um numero para a posição {pos}: "))
    l1.append(n)
    cont += 1
    pos += 1
print(f"Lista: {l1}")
somar = 0
print("---")
for i in range(len(l1)):
    somar += l1[i]
print(f"A soma dos elementos da lista é: {somar:.2f}")
print("\n")
print("-------------")
print("ii)")
alunos = {}
for i in range(1, 4):
    aluno = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[aluno] = nota
print(alunos)
soma_not = 0
for nota in alunos.values():
    soma_not += nota
print("Média da turma: ", soma_not/3)
print("\n")
print("-------------")
print("iii)")
soma_m = 0
matriz = np.array([[3, 4, 5],
                   [3, 1, 5]])
print(matriz)
print("---")
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma_m += (matriz[i][j])
print("A soma dos elementos da matriz é: ", soma_m)
print('#-----------------------------------------------#')
