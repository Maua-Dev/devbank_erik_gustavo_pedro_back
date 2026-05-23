from ..entities.user import User
from ..entities.transacao import Transacao

# mock armazena os dados de forma local
# self user cria um usuário fixo na memória e devolve o resultado no return
class UserRepositoryMock:

    user: User

    def __init__(self):

        self.user = User(
            name="Vitor Soller",
            agency="0000",
            account="00000-0",
            current_balance=1000.0
        )

    def get_user(self) -> User:
        return self.user

    def deposit(self, value: float) -> User:
        self.user.current_balance += value
        return self.user

    def withdraw( self, value: float) -> User:
        self.user.current_balance -= value
        return self.user