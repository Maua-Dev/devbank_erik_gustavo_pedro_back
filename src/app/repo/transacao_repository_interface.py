from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Union

from ..entities.transacao import Transacao

from ..enums.transaction_type_enum import TransactionTypeEnum

class ITransacaoRepository(ABC):
    __transacoes: List[Transacao]

    @abstractmethod
    def get_all_transactions(self) -> List[Transacao]:
        
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

    @abstractmethod
    def get_all_transactions_to_dict(self) -> Dict[str, List[Dict[str, Union[str, float, int]]]]:

        """

        Recupera todos as transacoes realizadas e as retorna em formato de dicionario, ordenadas por timestamp decrescente

        Tipo de retorno:
            Lista com objetos de Transacao

        """

        pass
