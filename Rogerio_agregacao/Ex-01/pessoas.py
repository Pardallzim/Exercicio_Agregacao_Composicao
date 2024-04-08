from gestao import Gestao
class Pessoa(Gestao):
    def __init__(self, nome:str, idade:int) -> None:
        super().__init__()
        self.nome = nome
        self.idade = idade
        self.cargo = ["Gerente","Funcionario","Auxiliar","Em teste"]

    def salario(self, cargo) ->int:
        if cargo == 0:
            self.salario = 3000.00
        elif cargo == 1:
            self.salario = 2000.00
        elif cargo == 2:
            self.salario = 1500.00
        else:
            self.salario = 1000.00

        return f"\n\nO {self.nome} de {self.idade} anos é {self.cargo[cargo]} descrição {self.descricao[cargo]} e seu salario é {self.salario}\n\n"