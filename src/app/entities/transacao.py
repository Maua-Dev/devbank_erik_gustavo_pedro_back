from ..enums.transaction_type_enum import TransactionTypeEnum
import datetime

class Transacao:
    type: TransactionTypeEnum
    value: float
    current_balance: float
    timestamp: int

    def __init__(self, type, value, current_balance, timestamp):
        if self.valida_tipo(type) == False:
            raise ValueError("O valor deve ser deposit ou withdraw.")
        else:
            self.type = self.valida_tipo(type)

        self.value = value
        self.current_balance = current_balance
        self.timestamp = int( datetime.now().timestamp() * 1000)


        

    def valida_tipo(self, tipo:str):
        try:
            tipo = TransactionTypeEnum(tipo)
            self.type = tipo
        
        except ValueError:
            raise ValueError(False)
        
    def validar_value(self, value):
        value = self.valida_tipo(value)
        if value <= 0:
            raise ValueError("O valor deve ser maior do que zero.")
        else:
            self.value = value
        
    def validar_current_balance(self, current_balance):
        if type(current_balance) != float:
            raise ValueError("O valor inserido é inválido.")
        else:
            if current_balance <= 0:
                raise ValueError("O valor deve ser maior do que zero.")
            else:
                self.current_balance = current_balance
        