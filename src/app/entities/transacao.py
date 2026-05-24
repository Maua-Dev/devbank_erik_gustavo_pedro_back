from ..enums.transaction_type_enum import TransactionTypeEnum
from datetime import datetime
from ..errors.entity_errors import ParamNotValidated

class Transacao:
    __type: TransactionTypeEnum
    __value: float
    __current_balance: float
    __timestamp: int

    def __init__(
            self,
            type: str,
            value: float, 
            current_balance: float, 
            ):
        
        self.type = type
        self.value = value
        self.current_balance = current_balance
        self.timestamp = int(datetime.now().timestamp() * 1000)

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, tipo):
        if not isinstance(tipo, str):
            raise ParamNotValidated("type", "must be of type str")
        try:
            tipo = TransactionTypeEnum(tipo)
            self.__type = tipo
        except ValueError:
            raise ParamNotValidated('type', 'invalid transaction type')
        
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        if self.valida_valores_numericos(value):
            self.__value = value
    
    @property
    def current_balance(self):
        return self.__current_balance
    @current_balance.setter
    def current_balance(self, current_balance):
        if self.valida_valores_numericos(current_balance):
            self.__current_balance = current_balance
    @property
    def timestamp(self):
        return self.__timestamp
    @timestamp.setter
    def timestamp(self, timestamp):
        if self.valida_valores_numericos(timestamp):
            self.__timestamp = timestamp

    def to_dict(self):
        return {
            'current_balance': self.current_balance,
            'timestamp': self.timestamp
        }
    
    def valida_valores_numericos(self, value: float):
        if not isinstance(value, (int, float)):
            raise ParamNotValidated('value', "must be a number")
        if value <= 0:
            raise ParamNotValidated("value", "must be greater than zero")
        
        return True