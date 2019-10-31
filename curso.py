class Curso():

    def __init__(self, nome, sigla, ativo):
        self.nome = nome
        self.sigla = sigla
        self.ativo = ativo


    def __str__(self):
        return '{} ({})'.format (self.nome, self.sigla)