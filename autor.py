class Autor:

    def __init__(self, nome, sobrenome, idade):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._posts = []
        self._leitores = []


    def add_post(self, post):
        if post not in self._posts:
            self._posts.append(post)
            
            for leitor in self._leitores:
                msg = f"O autor {self._nome} publicou um novo Post intitulado -> {post._titulo}"
                leitor.update(msg)
            
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
