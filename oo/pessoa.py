class Pessoa:
    olhos = 2
    def __init__(self, *filhos,nome=None,idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 26

    @classmethod
    def nome_e_atributo_de_classes(cls):
        return f'{cls} - Olhos: {cls.olhos}'

if __name__ == '__main__':
    abdael = Pessoa(nome='Abdael',idade=3)
    gabriel = Pessoa(abdael,nome='Gabriel')
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