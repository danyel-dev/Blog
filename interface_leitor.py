import abc

class abstract_Leitor(abc.ABC):

    @abc.abstractmethod
    def notificação(self, msg):
        """
        Esse método recebe uma mensagem e a imprime na tela.
        """   
