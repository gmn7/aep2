




from Aluno import Aluno

class Medio(Aluno):

    def __init__(self, codigoM, nomeM, matriculaM, anoM):
        Aluno.__init__(self, codigoM, nomeM, matriculaM)
        self.ano = anoM

    def imprimir_medio(self):
        Aluno.imprmir_aluno(self)
        print("Ano" +self.ano)


    @staticmethod
    def toMedio(aluno, ano):
        m = Aluno ( aluno.nome, aluno.matricula, ano)
        return m