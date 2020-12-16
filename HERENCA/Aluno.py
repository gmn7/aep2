class Aluno:

    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprmir_aluno(self):
        print("Nome: "+self.nome)
        print("Matricula: "+self.matricula)


    @staticmethod
    def toAluno(aluno):
        a = Aluno( aluno.codigo, aluno.nome, aluno.matricula)
        return a










