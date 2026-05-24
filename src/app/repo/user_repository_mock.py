from ..entities.user import User
from ..entities.transacao import Transacao

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