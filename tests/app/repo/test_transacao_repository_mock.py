import pydantic
import pytest
from typing import List, Dict 

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

    def test_add_transaction_invalid_type(self):
        user_repo = UserRepositoryMock()
        transacao_repo = TransacaoRepositoryMock()
        user = user_repo.get_user()

        with pytest.raises(ParamNotValidated):
            transacao_repo.add_transaction(10)


    def test_get_all_transactions_to_dict(self):
        user_repo = UserRepositoryMock()
        transacao_repo = TransacaoRepositoryMock()
        transferencias_dict = transacao_repo.get_all_transactions_to_dict()

        assert 'all_transactions' in transferencias_dict
        assert isinstance(transferencias_dict['all_transactions'], list)
        assert isinstance(transferencias_dict['all_transactions'][0], dict)
        assert len(transferencias_dict['all_transactions']) == 3



    def test_get_all_transactions_to_dict_order(self):
        user_repo = UserRepositoryMock()
        transacao_repo = TransacaoRepositoryMock()
        transferencias_dict = transacao_repo.get_all_transactions_to_dict()

        
        assert transferencias_dict['all_transactions'][0]['timestamp'] >= transferencias_dict['all_transactions'][1]['timestamp'] >= transferencias_dict['all_transactions'][2]['timestamp']
