class Pessoa:
	def __init__(self, nome, idade, altura):
		self.nome = nome
		self.idade = idade
		self.altura = altura

	def saudacao(self):
		print(f"Olá, {self.nome}!")

p1 = Pessoa("Nícolas", 18, 1.85)
p1.saudacao()
