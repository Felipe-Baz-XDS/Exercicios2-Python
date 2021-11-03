from Aluno import Aluno
from validateCPF import validateCPF
class Alunos:

    def __init__(self, lista):
        self.Lista = lista
    
    def getApproved(self):
        for Aluno in self.Lista:
            if Aluno.isApproved() == True:
                print(f"Aluno {Aluno.nome} foi aprovado")
    
    def getDisapproved(self):
        for Aluno in self.Lista:
            if Aluno.isApproved() !=True:
                print(f"Aluno {Aluno.nome} não foi aprovado")
    
    def getValidDocument(self):
        for Aluno in self.Lista:
            if validateCPF(Aluno.cpf):
                print(f"Aluno {Aluno.nome} CPF valido")

    def getUnderage(self):
        for Aluno in self.Lista:
            if Aluno.idade < 18:
                print(f"Aluno {Aluno.nome} é menor de idade")

if __name__ == '__main__':
    listaDeAlunos = []
    listaDeAlunos.append(Aluno("joão",18,"479.112.348-41", [6,6,6,6]))
    listaDeAlunos.append(Aluno("Maria",20,"479.132.358-41", [5,6,6,6]))
    listaDeAlunos.append(Aluno("Giovanna",16,"459.122.448-42", [10,10,10,10]))

    sistema = Alunos(listaDeAlunos)

    print("Aprovados")
    sistema.getApproved()
    print("reprovados")
    sistema.getDisapproved()
    print("menores de idade")
    sistema.getUnderage()
    print("documentos validos")
    sistema.getValidDocument()

