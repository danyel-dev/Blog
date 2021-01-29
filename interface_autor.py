import abc

class abstract_Autor(abc.ABC):

    @abc.abstractmethod
    def add_post(self, post):
        """
        Esse método adiciona um objeto do tipo
        Post que é passado por parâmetro na lista
        de Posts, e em seguida passa uma mensagem 
        para cada leitor de que o Post foi adicionado.
        """


    @abc.abstractmethod
    def remove_post(self, post):
        """
        Esse método remove um objeto do tipo
        Post que é passado por parâmetro da lista de Posts.
        """ 


    @abc.abstractmethod
    def add_leitor(self, leitor):
        """
        Esse método recebe um objeto do tipo leitor
        que é passado por parâmetro e em seguida 
        adiciona na lista de leitores caso esse leitor exista.
        """ 


    @abc.abstractmethod
    def remove_leitor(self, leitor):
        """
        Esse método recebe um objeto do tipo leitor
        que é passado por parâmetro e em seguida o 
        remove da lista de leitores caso esse leitor exista.
        """ 


    @abc.abstractmethod
    def atualizar_post(self, titulo):
        """
        Esse método atualiza um post
        """
