class Leitor:

    def __init__(self, nome, sobrenome, idade):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade


    def update(self, msg):
        print(f"Olá {self._nome}, você tem a seguinte mensagem:\n{msg}")
        print("\n")
