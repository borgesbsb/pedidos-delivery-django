class Pedido():
    def __init__(self, cliente, observacoes, data_pedido, valor, status, produto):
        self.__cliente = cliente
        self.__observacoes = observacoes 
        self.__data_pedido = data_pedido
        self.__valor = valor
        self.__status = status
        self.__produto = produto

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
        
    @property
    def observacoes(self):
        return self.__observacoes

    @observacoes.setter
    def observacoes(self, observacoes):
        self.__observacoes = observacoes
        
    @property
    def data_pedido(self):
        return self.__data_pedido

    @data_pedido.setter
    def data_pedido(self, data_pedido):
        self.__data_pedido = data_pedido

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

