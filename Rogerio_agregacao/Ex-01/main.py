from pessoas import Pessoa



nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))

cargo = int(input("\n\nDigite 0 para 'Gerente', 1 para 'Funcionario', 2 para 'Auxiliar' e 3 para 'Em teste': "))

x = Pessoa(nome, idade)

print(x.salario(cargo))

