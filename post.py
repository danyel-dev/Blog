class autor:

    def __init__(self, nome, idade, sexo):
        self._nome = nome
        self._idade = idade
        self._sexo = sexo
        self._posts = []
        self._leitores = []


    def add_post(self, leitor):
        ...


    def remove_post(self, leitor):
        ...


    def add_leitor(self, leitor):
        ...


    def remove_leitor(self, leitor):
        ...


    def notifica_leitor(self, msg):
        ...


class Post:

    def __init__(self, titulo, data, autor, categoria):
        self._titulo = titulo
        self._data = data
        self._data_atualizada = data_atualizada
        self._categoria = []   
        self._comentario = []
    

    def imprime_post(self):
        ...


    def add_comentario(self, comentario):
        ...


    def add_categoria(self, categoria)
        ...
    