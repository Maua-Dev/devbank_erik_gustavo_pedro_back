from pydantic import ValidationError
import pytest

from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Dict
from src.app.entities.transacao import Transacao, ParamNotValidated
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.entities.user import User


class Test_Transacao:
    def test_transacao_construtor(self):
        t1 = Transacao(
            user=User('Vitor Soller', '0000', '00000-0', 1000.0),
            type='deposit',
            value=100.0,
        )

        assert t1
        assert t1.type.value == 'deposit'
        assert t1.value == 100
        assert t1.current_balance == 1100
        assert t1.timestamp == int(datetime.now(tz=ZoneInfo('America/Sao_Paulo')).timestamp() * 1000)

    def test_transacao_error_user(self):
        with pytest.raises(ParamNotValidated):
            t1 = Transacao(
                user='Vitor Soller',
                type='deposit',
                value=100.0,
            )

    def test_transacao_error_type(self):
        with pytest.raises(ParamNotValidated):
            t1 = Transacao(
                user=User('Vitor Soller', '0000', '00000-0', 1000.0),
                type='d',
                value= 100,
            )
    def test_transacao_error_value(self):
        with pytest.raises(ParamNotValidated):
            t1 = Transacao(
                user=User('Vitor Soller', '0000', '00000-0', 1000.0),
                type='deposit',
                value= '100*a',
            )
    def test_transacao_error_current_balance(self):
        with pytest.raises(Exception):
            t1 = Transacao(
                user=User('Vitor Soller', '0000', '00000-0', 1000.0),
                type='deposit',
                value= 100,
                current_balance= '*****'
            )
    def test_transacao_error_timestamp(self):
        with pytest.raises(Exception):
            t1 = Transacao(
                user=User('Vitor Soller', '0000', '00000-0', 1000.0),
                type = 'withdraw',
                value = 100,
                timestamp= 30
            )

    def test_transacao_deposit(self):
        user = User('Vitor Soller', '0000', '00000-0', 1000.0)
        t1 = Transacao(
            user=user,
            type='deposit',
            value=100.0,
        )

        assert t1.current_balance == 1100
        assert user.current_balance == 1100
    def test_transacao_withdraw(self):
        user = User('Vitor Soller', '0000', '00000-0', 1000.0)
        t1 = Transacao(
            user=user,
            type='withdraw',
            value=100.0,
        )
        assert t1.current_balance == 900
        assert user.current_balance == 900


    def test_transacao_to_dict(self):
        t1 = Transacao(
            user=User('Vitor Soller', '0000', '00000-0', 1000.0),
            type='deposit',
            value=100.0,
        )

        t1_dict = t1.to_dict()

        assert isinstance(t1_dict, dict)
        assert t1_dict == {'current_balance': 1100, 'timestamp':  int(datetime.now(tz=ZoneInfo('America/Sao_Paulo')).timestamp() * 1000)}

    def test_transacao_to_dict_history(self):
        t1 = Transacao(
            user=User('Vitor Soller', '0000', '00000-0', 1000.0),
            type='deposit',
            value=100,
        )

        t1_dict_history = t1.to_dict_history()

        assert isinstance(t1_dict_history, dict)
        assert t1_dict_history == {
            'type': 'deposit',
            'value': 100,
            'current_balance': 1100,
            'timestamp': int(datetime.now(tz=ZoneInfo('America/Sao_Paulo')).timestamp() * 1000)
        }
