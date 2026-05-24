from pydantic import ValidationError
import pytest

from src.app.entities.user import User


class Test_User:
    def test_user(self):
        user = User(
            name='test',
            agency='0000',
            account='0000-0',
            current_balance=1000.0
        )
        assert user.name == 'test'
        assert user.agency == '0000'
        assert user.account == '0000-0'
        assert user.current_balance == 1000.0

    def test_to_dict(self):
        user = User(
            name='test',
            agency='0000',
            account='0000-0',
            current_balance=1000.0
        )
        dic = user.to_dict()
        
        assert dic['name'] == 'test'
        assert dic['agency'] == '0000'
        assert dic['account'] == '0000-0'
        assert dic['current_balance'] == 1000.0

