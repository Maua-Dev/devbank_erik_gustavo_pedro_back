from pydantic import ValidationError
import pytest

from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated

# testes em caso de dados validados corretamente 
class Test_User:
    def test_user(self):
        user = User(
            name='test',
            agency='0000',
            account='00000-0',
            current_balance=1000.0
        )
        assert user.name == 'test'
        assert user.agency == '0000'
        assert user.account == '00000-0'
        assert user.current_balance == 1000.0

    def test_to_dict(self):
        user = User(
            name='test',
            agency='0000',
            account='00000-0',
            current_balance=1000.0
        )
        dic = user.to_dict()
        
        assert dic['name'] == 'test'
        assert dic['agency'] == '0000'
        assert dic['account'] == '00000-0'
        assert dic['current_balance'] == 1000.0

# Testes em caso de falha na validação dos parâmetros

    def test_invalid_agency(self):
        with pytest.raises(ParamNotValidated):

            User(
                name='test',
                agency='12',
                account='00000-0',
                current_balance=1000.0
            )
    
    def test_invalid_account(self):
        with pytest.raises(ParamNotValidated):

            User(
                name='test',
                agency='0000',
                account='123',
                current_balance=1000.0
            )
    
    def test_invalid_balance(self):
        with pytest.raises(ParamNotValidated):
                User(
                    name='test',
                    agency='0000',
                    account='00000-0',
                    current_balance=-100
                )
    
    def test_invalid_name(self):
        with pytest.raises(ParamNotValidated):
            User(
                name='aa',
                agency='0000',
                account='00000-0',
                current_balance=1000.0
            )

