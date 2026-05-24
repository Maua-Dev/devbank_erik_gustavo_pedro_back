from .transacao_repository_interface import ITransacaoRepository
from ..entities.transacao import Transacao
from ..errors.entity_errors import ParamNotValidated

from typing import Optional, List

from datetime import datetime

class TransacaoRepositoryMock(ITransacaoRepository):
    __transacoes: List[Transacao]

    def __init__(self, transacoes: List[Transacao]) -> None:
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

    def get_all_transactions(self) -> Optional[List[Transacao]]:
        return self.__transacoes
    
    def add_transaction(self, transacao: Transacao) -> None:
        if not isinstance(transacao, Transacao):
            raise ParamNotValidated('transaction', 'must be of type Transacao')
        self.__transacoes.append(transacao)