print("\n")
print("-----------")
class Aluno:

    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def puts(self):
        return self.nome
        return self.nota1
        return self.nota2

    def media(self):
        self.result_media = (self.nota1 + self.nota2) / 2
        return self.result_media

    def aprovado_reprovado(self):
        if self.result_media >= 6:
            print('Aprovado')
        else:
            print("Esta reprovado")

joaozinho = Aluno('Joao', 6, 5)
print(joaozinho.puts())
print("---")
print(joaozinho.media())
print("---")
joaozinho.aprovado_reprovado()
print("-----------")
