from interface_leitor import abstract_Leitor

class Leitor(abstract_Leitor):

    __slots__ = ["_nome", "_sobrenome", "_idade"]


    def __init__(self, nome, sobrenome, idade):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade


    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, nome):
        self._nome = nome


    @property
    def sobrenome(self):
        return self._sobrenome


    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome


    @property
    def idade(self):
        return self._idade


    @idade.setter
    def idade(self, idade):
        self._idade = idade


    def notificação(self, msg):
        print(f"Olá {self._nome}, você tem a seguinte mensagem:\n{msg}")
        print("\n")
