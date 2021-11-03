class Aluno:

    def __init__(self, nome, idade, cpf, notas):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.notas = notas
    

    def toString(self):
        print(f"Aluno {self.nome} tem {self.idade} anos\n")
        return
    

    def isApproved(self):
        count = 0
        for i in self.notas:
            count += i
        if count/(len(self.notas)) >= 6:
            return True
        return False


if __name__ == '__main__':
    lista = [7.5,9,10, 0]
    aluno = Aluno("João", 19, "046.629.120-59", lista)
    print(aluno.isApproved())
    print(aluno.toString())
    print("fim")
