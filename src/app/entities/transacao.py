from typing import Dict, Optional
from zoneinfo import ZoneInfo
from datetime import datetime
from ..entities.user import User
from ..enums.transaction_type_enum import TransactionTypeEnum
from ..errors.entity_errors import ParamNotValidated

class Transacao:
    __user = User
    __type: TransactionTypeEnum
    __value: float
    __current_balance: float
    __timestamp: int

    def __init__( 
            self,
            user: User,
            type: str,
            value: float,  
            ):
        
        self.user = user
        self.type = type
        self.value = value
        self.current_balance = user.current_balance + value if type == 'deposit' else user.current_balance - value
        self.timestamp = int(datetime.now(tz=ZoneInfo('America/Sao_Paulo')).timestamp() * 1000)

        user.current_balance = self.current_balance


    @property    
    def user(self):
        return self.__user
    @user.setter
    def user(self, user) -> Optional[None]:
        if not isinstance(user, User):
            raise ParamNotValidated('user', 'must be of type User')
        self.__user = user

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, tipo) -> Optional[None]:
        if not isinstance(tipo, str):
            raise ParamNotValidated("type", "must be of type str")
        try:
            tipo = TransactionTypeEnum(tipo)
            self.__type = tipo
        except ValueError:
            raise ParamNotValidated('type', 'invalid transaction type')
        
    @property
    def value(self) -> float | int:
        return self.__value
    @value.setter
    def value(self, value) -> Optional[None]:
        value = self.valida_valores_numericos(value, 'value')
        if value > self.user.current_balance and self.type.value == 'withdraw':
            raise ParamNotValidated('value', 'insufficient balance for withdrawal')
        if value > self.user.current_balance * 2 and self.type.value == 'deposit':
            raise ParamNotValidated('value', 'suspicious deposit')
        self.__value = value
    
    @property
    def current_balance(self) -> float | int:
        return self.__current_balance
    @current_balance.setter
    def current_balance(self, current_balance) -> Optional[None]:
            current_balance = self.valida_valores_numericos(current_balance, 'current_balance')
            self.__current_balance = current_balance
    @property
    def timestamp(self) -> int:
        return self.__timestamp
    @timestamp.setter
    def timestamp(self, timestamp) -> Optional[None]:
        if not isinstance(timestamp, int):
            raise ParamNotValidated('timestamp', 'must be of tipe int')
        
        if timestamp < 0:
            raise ParamNotValidated('timestamp', 'must be a positive number')
        self.__timestamp = timestamp

    def to_dict(self) -> Dict[str, float | int]:
        return {
            'current_balance': self.current_balance,
            'timestamp': self.timestamp
        }

    def to_dict_history(self) -> Dict[str, str | float | float | int]:
        return {
            'type': self.type.value,
            'value': self.value,
            'current_balance': self.current_balance,
            'timestamp': self.timestamp
        }
    
    
    def valida_valores_numericos(self, value: float | int, param: str) -> int | float:
        try:
                value = float(value)
        except:
            raise ParamNotValidated(param, 'must be a number')
        
        if param == 'value' and value <= 0 :
            raise ParamNotValidated(param, "must be greater than zero")
        
        return value
