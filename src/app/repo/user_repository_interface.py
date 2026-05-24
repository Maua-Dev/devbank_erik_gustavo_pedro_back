from abc import ABC, abstractmethod
from ..entities.user import User
from ..entities.transacao import Transacao



class IUserRepositoryInterface(ABC):
    user: User
    
    @abstractmethod
    def get_user() -> User:
        """
        Recupera o usuario

        Tipo de retorno:
            Objeto da classe User
        """

        pass