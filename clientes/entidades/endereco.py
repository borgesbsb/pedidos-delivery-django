class Endereco():
    def __init__(self, rua, numero, complemento, bairro, cidade, pais ):
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__pais = pais
    
    @property
    def rua(self):
        return self.__rua
    
    @rua.setter
    def rua(self, rua):
        self.__rua = rua
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero    
        
    @property
    def complemento(self):
        return self.__complemento
    
    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento
        
    @property
    def bairro(self):
        return self.__bairro
    
    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro
        
    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade
        
    @property
    def pais(self):
        return self.__pais
    
    @pais.setter
    def pais(self, pais):
        self.__pais = pais    
        
        
        
        