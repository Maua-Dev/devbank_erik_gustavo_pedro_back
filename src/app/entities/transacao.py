from ..enums.transaction_type_enum import TransactionTypeEnum

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
        self.timestamp = timestamp

        

    def valida_tipo(self, tipo:str):
        try:
            tipo = TransactionTypeEnum(tipo)
            return tipo
        
        except ValueError:
            raise ValueError(False)
        
print(Transacao("A"))