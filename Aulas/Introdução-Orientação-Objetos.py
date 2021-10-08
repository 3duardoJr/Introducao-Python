print("\n")
print("--------")
class Quadrados:
    def __init__(self, lado1, lado2, lado3, lado4):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4

    def verificaçao(self, lado1, lado3):
        if self.lado1 != self.lado3:
            print("Não é um quadrado")
        else:
            print("É um quadrado")

    def area(self, lado1, lado2):
        result = lado1 * lado2
        return result


retangulo = Quadrados(2, 4, 2, 4)
retangulo.verificaçao(retangulo.lado1, retangulo.lado3)
print("---")
print(retangulo.area(retangulo.lado1, retangulo.lado2))
print("--------")
