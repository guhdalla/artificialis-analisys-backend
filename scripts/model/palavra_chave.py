class PalavraChave:

    def __init__(self):
        pass

    def __init__(self, id, score, texto, inicio, fim, id_pesquisa):
        self.id = id
        self.score = score
        self.texto = texto
        self.inicio = inicio
        self.fim = fim
        self.id_pesquisa = id_pesquisa

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id


    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def texto(self):
        return self.__texto
    
    @texto.setter
    def texto(self, texto):
        self.__texto = texto
    
    @property
    def inicio(self):
        return self.__inicio
    
    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio

    @property
    def fim(self):
        return self.__fim
    
    @fim.setter
    def fim(self, fim):
        self.__fim = fim

    @property
    def id_pesquisa(self):
        return self.__id_pesquisa
    
    @id_pesquisa.setter
    def id_pesquisa(self, id_pesquisa):
        self.__id_pesquisa = id_pesquisa

    def converter_in_comprehend(result, id_pesquisa):
        return PalavraChave(None, result["Score"], result["Text"], result["BeginOffset"], result["EndOffset"], id_pesquisa)