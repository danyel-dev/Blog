class Post:

    __slots__ = ["_titulo", "_data", "_data_atualizacao", "_conteudo"]


    def __init__(self, titulo, data, data_atualizacao, conteudo):
        self._titulo = titulo
        self._data = data
        self._data_atualizacao = data_atualizacao
        self._conteudo = conteudo


    @property
    def titulo(self):
        return self._titulo

    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo


    @property
    def data(self):
        return self._data

    
    @data.setter
    def data(self, data):
        self._data = data


    @property
    def data_atualizacao(self):
        return self._data_atualizacao

    
    @data_atualizacao.setter
    def data_atualizacao(self, data_atualizacao):
        self._data_atualizacao = data_atualizacao
    

    @property
    def conteudo(self):
        return self._conteudo

    
    @conteudo.setter
    def conteudo(self, conteudo):
        self._conteudo = conteudo


    def imprimir_post(self):
        print(f"Título: {self._titulo}")
        print(f"Data do post: {self._data}")
        print(f"Ultima atualização: {self._data_atualizacao}\n")
        print(self._conteudo)


    def update(self, conteudo, data_atualizacao):
        self._conteudo = conteudo
        self._data_atualizacao = data_atualizacao


if __name__ == "__main__":
    print("oi")
