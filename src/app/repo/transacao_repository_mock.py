from .transacao_repository_interface import ITransacaoRepository
from ..entities.transacao import Transacao
from ..errors.entity_errors import ParamNotValidated

from typing import Optional, Dict, List

from datetime import datetime

class TransacaoRepositoryMock(ITransacaoRepository):
    __transacoes: list[Transacao]

    def __init__(self, transacoes: list[Transacao]) -> None:
        self.transacoes = [
            Transacao(
                type='deposit',
                value=1000.0,
                current_balance=1000.0
                ),
            Transacao(
                type='withdraw',
                value=100.0,
                current_balance=900.0
            ),
            Transacao(
                type='deposit',
                value=200.0,
                current_balance=1100.0
            )
        ]

    @property
    def transacoes(self):
        return  self.__transacoes     
    @transacoes.setter
    def transacoes(self, transacoes: list[Transacao]):
        if not all(isinstance(transacao, Transacao) for transacao in transacoes):
            raise ParamNotValidated('transacoes', 'must contain only Transacao instances')
        self.__transacoes = transacoes

    def get_all_transactions(self) -> Optional[List[Transacao]]:

        return super().get_all_transactions()
