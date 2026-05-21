from typing import Tuple

# Adiciona Caracteristicas do usuário (nome, agencia, conta e saldo)

class User:

    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(
        self,
        name: str,
        agency: str,
        account: str,
        current_balance: float
    ):

        validation_name = self.validate_name(name)
        if not validation_name[0]:
            raise ValueError(validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency)
        if not validation_agency[0]:
            raise ValueError(validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account)
        if not validation_account[0]:
            raise ValueError(validation_account[1])
        self.account = account

        validation_balance = self.validate_balance(current_balance)
        if not validation_balance[0]:
            raise ValueError(validation_balance[1])
        self.current_balance = current_balance

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:

        if name is None:
            return (False, "Name is required")

        if type(name) != str:
            return (False, "Name must be string")

        return (True, "")

    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:

        if agency is None:
            return (False, "Agency is required")

        if type(agency) != str:
            return (False, "Agency must be string")

        if len(agency) != 4:
            return (False, "Agency must contain 4 digits")

        return (True, "")

    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:

        if account is None:
            return (False, "Account is required")

        if type(account) != str:
            return (False, "Account must be string")

        return (True, "")

    @staticmethod
    def validate_balance(balance: float) -> Tuple[bool, str]:

        if balance is None:
            return (False, "Balance is required")

        if type(balance) not in [float, int]:
            return (False, "Balance must be numeric")

        return (True, "")

    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }