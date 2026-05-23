from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Union

from ..entities.transacao import Transacao

from ..enums.transaction_type_enum import TransactionTypeEnum

class ITransacaoRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> list[Transacao]:
        
        """

        Recupera todos as transacoes realizadas

        Tipo de retorno:
            Lista com objetos de Transacao

        """
        
        pass

    @abstractmethod
    def add_transaction(self, transacao: Transacao) -> None:

        """
        Adiciona uma transacao ao repositorio

        Args:
            transacao (Transacao): Objeto de Transacao
        
        """
        pass

