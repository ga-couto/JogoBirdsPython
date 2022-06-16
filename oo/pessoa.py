class Pessoa:
    olhos = 2
    def __init__(self, *filhos,nome=None,idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá, meu nome é: {self.nome} e o ID é: {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 26

    @classmethod
    def nome_e_atributo_de_classes(cls):
        return f'{cls} - Olhos: {cls.olhos}'
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão!'
class Mutante(Pessoa):
    olhos = 4
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de antenas!'


if __name__ == '__main__':
    abdael = Homem(nome='Abdael',idade=3)
    gabriel = Pessoa(abdael,nome='Gabriel Couto')
    mutante = Mutante(nome='Alienigena')
    print(Pessoa.cumprimentar(gabriel))
    print(id(gabriel))
    print(gabriel.cumprimentar())
    print(gabriel.nome)
    print(gabriel.idade)
    for filhos in abdael.filhos:
        print(filhos.nome)
    gabriel.sobrenome = 'Couto'
    abdael.sobrenome = 'Couto'
    del gabriel.filhos
    print(gabriel.__dict__)
    print(abdael.__dict__)
    print(Pessoa.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos))
    print(Pessoa.metodo_estatico(), gabriel.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classes(), gabriel.nome_e_atributo_de_classes())
    print('---------------------')
    pessoa = Pessoa('Anonima')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa,Homem))
    homem = Homem('Anonima')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print('---------------------')
    print(f'Olhos: {mutante.olhos}')
    print('---------------------')
    print(gabriel.cumprimentar())
    print(abdael.cumprimentar())
    print(mutante.cumprimentar())