print("\n")
print("----------Funções----------")


def mensagem():
    print("Mensagem de Texto")


mensagem()

print("---")


def mensagem1(texto):
    print(texto)


mensagem1("alibaba")

print("---")


def calcula_energia_potencial_gravitacional(m, h, g=10):

    '''
    --------------------------------------------------------
    Argumentos:
    m: massa, entrada como variável float
    h: altura, entra com uma variável float

    Argumetos Opcionais:
    g: aceleração gravitacional, com o valor default de 10
    --------------------------------------------------------
    '''

    e = g * m * h
    return e


r = calcula_energia_potencial_gravitacional(30, 12)
print(r)

print("---")

help(calcula_energia_potencial_gravitacional)

print("---------------------------")
