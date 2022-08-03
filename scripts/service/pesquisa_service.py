from repository.pesquisa_repository import PesquisaRepository

class PesquisaService:

    def __init__(self):
        self.repository = PesquisaRepository()

    def listar(self, size, offset, palavraChave, sentimento, nps):
        return self.repository.listar(size, offset, palavraChave, sentimento, nps)
