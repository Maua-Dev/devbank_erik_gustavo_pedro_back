from typing import Tuple, Dict
from ..errors.entity_errors import ParamNotValidated
import re

# validações dos atributos do usuario (name, agency, account e current balance)
class User:

    __name: str
    __agency: str
    __account: str
    __current_balance: float

    def __init__(
        self,
        name: str,
        agency: str,
        account: str,
        current_balance: float
    ):
        self.name = name
        self.agency = agency
        self.account = account
        self.current_balance = current_balance

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.valida_valores_str(name, 'name')
        if not 3 <= len(name) <= 40:
            raise ParamNotValidated('name', 'must be greater than 3 and less than 40')
        self.__name = name

    @property
    def agency(self):
        return self.__agency

    @agency.setter
    def agency(self, agency: str):
        self.valida_valores_str(agency, 'agency')
        if not re.match(r"^\d{4}$", agency):
            raise ParamNotValidated('agency', 'must be in the format 0000')
        self.__agency = agency

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, account: str):
        self.valida_valores_str(account, 'account')
        if not re.match(r"^\d{5}-\d$", account):
            raise ParamNotValidated('account', 'must be in the format 00000-0')
        self.__account = account
    
    @property
    def current_balance(self):
        return self.__current_balance
    @current_balance.setter
    def current_balance(self, current_balance: float):
        if not isinstance(current_balance, (float, int)):
            raise ParamNotValidated('current balance', 'must be of type float')
        if not current_balance >= 0:
            raise ParamNotValidated('current balance', 'must be greater than zero')
        self.__current_balance = current_balance


    @staticmethod
    def valida_valores_str(string: str, param_name: str) -> None:
        if not string:
            raise ParamNotValidated(param_name, 'is required')
        if not isinstance(string, str):
            raise ParamNotValidated(param_name, 'must be of type str')

    def to_dict(self) -> Dict[str, str | str | str | float]:
        name = self.name
        agency = self.agency
        account = self.account
        current_balance = self.current_balance

        return {
            "name":name,
            "agency":agency,
            "account":account,
            "current_balance":current_balance
        }
    
    def __str__(self) -> str:
        return f"User(name={self.name}, agency={self.agency}, account={self.account}, current_balance={self.current_balance})"