from datetime import datetime

class History:
    __transacoes: list[Transacao]

    def __init__(self, transacoes: list[Transacao]) -> None:



    @property
        def transacoes(self):
            return self.transacoes
    @transacoes.setter
        def set_transacoes(self, transacoes: list):
            if transacoes:
                for i, transacao in enumerate(transacoes):
                    self.transacoes.append()
            else: 