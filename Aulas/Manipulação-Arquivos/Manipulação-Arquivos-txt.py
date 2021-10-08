print("\n")
print("----------")
with open('./Teste.txt') as tex:
    for linha in tex:
        print(linha)
print("---")
with open('./Teste.txt') as tex:
    r = tex.readlines()
    print(r)
print("---")
with open('Teste2.txt', 'w') as texto:
    texto.write("Criando um arquivo de texto pelo python")  # Criando
# ----------------------------------------------------------
with open('./Teste2.txt', 'r') as texto:                    # Lendo
    reader = texto.readline()
    print(reader)
print("----------")
