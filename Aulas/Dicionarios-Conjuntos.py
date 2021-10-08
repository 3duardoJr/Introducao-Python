print("\n")
print('#-------------------------------------------------Dicionários-------------------------------------------------#')
mem_guild = {'Suporte': 3, 'DPS Melee': 2, 'DPS Ranged': 4, 'DPS Magico': 1, 'Tank': 3}
print(mem_guild['Suporte'])
print('----------------')
mem_guild['Sup Melee'] = 2
mem_guild['Druida'] = 1
print(mem_guild)
print('----------------')
del(mem_guild['Druida'])
print(mem_guild)
print('----------------')
print(mem_guild.items())
print(mem_guild.keys())
print(mem_guild.values())
print('----------------')
mem_guild_new = {'Assassino': 3}
mem_guild.update(mem_guild_new)
print(mem_guild)
print('----------------')
for classe, player_class in mem_guild.items():
    print(f"Classe: {classe}, Numero de jogadores com essa classe: {player_class}")
print('#-------------------------------------------------------------------------------------------------------------#')
print("\n")
print("#-------------------------Conjuntos------------------------#")
# Mostrando apenas as chaves que não se repetem no dicionario
mem_guild = {'Suporte': 3, 'DPS Melee': 2, 'DPS Ranged': 4, 'DPS Magico': 1, 'Tank': 3, 'DPS Magico': 1, 'DPS Magico': 1}
print(set(mem_guild))
print('----------------')
c1 = {1, 2, 3, 4, 5}
c2 = {4, 5, 6, 7, 8}
c3 = c1.intersection(c2)  # Mostrando onde eles se intersectam, ou seja, onde se repetem
print(c3)
print('----------------')
print(c1.difference(c2))  # A diferença entre os dois conjuntos
print("#----------------------------------------------------------#")
