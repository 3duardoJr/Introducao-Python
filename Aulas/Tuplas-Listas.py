print("\n")
print("#------Tuplas------#")
tupla = ('Ladino', 'Mago', 'Guerreiro', 'Druida', 'Clérigo')
print(tupla[1])
print("--------------------")
print(tupla.index('Druida'))
print("--------------------")
print("\n")
print("#----------------------------Listas----------------------------#")
l1 = ['Ladino', 'Mago', 'Guerreiro']
l2 = ['Monge', 'Druida', 'Clérigo']
l3 = l1 + l2  # Concatenando
print(l3)
print("--------------------")
print(l1[0])
print("--------------------")
print(l1[0:4])
print("--------------------")
l1.append('Ranger')
print(l1)
print("--------------------")
l1.remove('Guerreiro')  # Já para deletar uma lista inteira se usa o 'del', ex.: del(l1)
print(l1)
print("--------------------")