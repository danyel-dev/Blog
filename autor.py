from interface_autor import abstract_Autor

class Autor(abstract_Autor):

    __slots__ = ["_nome", "_sobrenome", "_idade", "_posts", "_leitores"]


    def __init__(self, nome, sobrenome, idade):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._posts = []
        self._leitores = []


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


    @property
    def posts(self):
        return self._posts


    @property
    def leitores(self):
        return self._leitores


    def add_post(self, post):
        if post not in self._posts:
            self._posts.append(post)
            
            for leitor in self._leitores:
                msg = f"O autor {self._nome} publicou um novo Post intitulado -> {post._titulo}"
                leitor.notificação(msg)
            return True

        return False        


    def remove_post(self, post):
        if post in self._posts:
            self._posts.remove(post)
            return True
        return False


    def add_leitor(self, leitor):
        if leitor not in self._leitores:
            self._leitores.append(leitor)
            return True
        return False


    def remove_leitor(self, leitor):
        if leitor in self._leitores:
            self._leitores.remove(leitor)
            return True
        return False


    def atualizar_post(self, titulo):
        for post in self._posts:
            if titulo == post.titulo:
                msg = "Lorem Ipsum é simplesmente um texto fictício da indústria de impressão e composição."
                post.update(msg, "203914")

                for leitor in self._leitores:
                    msg = f"O autor {self._nome} atualizou o Post intitulado -> {post._titulo}"
                    leitor.notificação(msg)
