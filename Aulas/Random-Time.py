import random as rm
import time
import time as tm

print("\n")
print("--------------------------------------")
print(rm.random())
print("---")
print(rm.randint(1, 10))
print("---")
print(rm.randrange(0, 10, 2))  # Um bom exemplo de como gerar números pares numa faixa determinada
print("---")
x = ["a", "b", 3, 4.4, "alibaba"]
print(rm.choice(x))
print("------")
print(tm.time())
print("---")
antes = tm.time()
lista = []
for i in range(0, 100000):
    lista.append(i)
depois = tm.time()
intervalo = depois - antes
print(f"A função foi executada em {intervalo:.2f}s")
print("---")
print("Finalizando...")
time.sleep(2)
print("...")
time.sleep(1)
print("Até a próxima")
