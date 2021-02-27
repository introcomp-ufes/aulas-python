class Usuario:
    def __init__(self, nome, idade, aniversario):
        self.nome = nome
        self.idade = idade
        self.aniversario = aniversario

    def maiorDeIdade(self):
        if self.idade > 18:
            return True
        else:
            return False

    def imprimeAniversario(self):
        print("O aniversário de " + self.nome + " é dia " + self.aniversario)