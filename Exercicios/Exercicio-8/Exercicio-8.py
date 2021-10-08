print("\n")
print("-----------")
alunos = {'Joao': 8, 'Eduardo': 10, 'DJ Rogeirinho': 0}
with open('Alunos.txt', 'w') as txt:
    for aluno, nota in alunos.items():
        txt.write(f"{aluno} : {nota}\n")
#--------------------------------------
with open('Alunos.txt') as txt:
    for linha in txt:
        print(linha)
print("-----------")