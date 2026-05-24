from .transacao_repository_interface import ITransacaoRepository
from ..entities.transacao import Transacao
from ..entities.user import User
from .user_repository_mock import UserRepositoryMock
from ..errors.entity_errors import ParamNotValidated

from typing import Optional, List, Dict

from datetime import datetime

class TransacaoRepositoryMock(ITransacaoRepository):

    def __init__(self) -> None:
        self.transacoes = [
            Transacao(
                user = UserRepositoryMock().get_user(),
                type='deposit',
                value=1000.0,
            ),
            Transacao(
                user = UserRepositoryMock().get_user(),
                type='withdraw',
                value=100.0,
            ),
            Transacao(
                user = UserRepositoryMock().get_user(),
                type='deposit',
                value=200.0,
            )
        ]

    def get_all_transactions(self) -> List[Transacao]:
        return self.transacoes
    
    def add_transaction(self, transacao: Transacao) -> None:
        if not isinstance(transacao, Transacao):
            raise ParamNotValidated('transaction', 'must be of type Transacao')
        self.transacoes.append(transacao)


    def get_all_transactions_to_dict(self) -> Dict[str, List[Dict[str, str | float | int]]]:
        dict = {
            'all_transactions': sorted([transacao.to_dict_history() for transacao in self.transacoes], key=lambda x: x['timestamp'], reverse=True)
        }
        return dict