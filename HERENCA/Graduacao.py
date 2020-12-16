from  Aluno import Aluno

class Graduacao(Aluno):

    def __init__(self, codigoG, nomeG, matriculaG, semestreG ):
        Aluno.__init__(self, codigoG, nomeG, matriculaG)
        self.semestre = semestreG

    def imprimir_graduacao(self):
        Aluno.imprmir_aluno(self)
        print("Semestre: " +self.semestre)


    @staticmethod
    def toGraduacao(aluno, semestre):
        g = Aluno ( aluno.nome, aluno.matricula, semestre)
        return g