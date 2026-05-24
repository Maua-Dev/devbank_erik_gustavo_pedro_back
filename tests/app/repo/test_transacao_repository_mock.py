import pydantic
import pytest


from src.app.entities.transacao import Transacao
from src.app.repo.transacao_repository_mock import TransacaoRepositoryMock
from src.app.repo.user_repository_mock import UserRepositoryMock
from src.app.errors.entity_errors import ParamNotValidated


class Test_TransacaoRepositoryMock:

    def test_get_all_transactions(self):
        user_repo = UserRepositoryMock()
        transacao_repo = TransacaoRepositoryMock()
        transacoes = transacao_repo.get_all_transactions()
        assert len(transacoes) == 3

    def test_add_transaction(self):
        user_repo = UserRepositoryMock()
        transacao_repo = TransacaoRepositoryMock()
        user = user_repo.get_user()

        transacao = Transacao(
            user=user,
            type='deposit',
            value=500.0,
        )
        transacao_repo.add_transaction(transacao)
        assert transacao in transacao_repo.get_all_transactions()