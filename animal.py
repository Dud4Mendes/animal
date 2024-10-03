# Classe base
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("O animal faz um som.")

    def apresentar(self):
        print(f"Eu sou um animal chamado {self.nome}")

# Classe derivada
class Cachorro(Animal):
    def emitir_som(self):
        print(f"O cachorro {self.nome} late: Au Au!")

# Outra classe derivada
class Gato(Animal):
    def emitir_som(self):
        print(f"O gato {self.nome} mia: Miau!")

# Classe principal
if __name__ == "__main__":
    cachorro = Cachorro("Rex")
    gato = Gato("Mimi")

    cachorro.apresentar()
    cachorro.emitir_som()

    gato.apresentar()
    gato.emitir_som()
