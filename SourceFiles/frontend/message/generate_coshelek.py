from .coshelek_message import data

def generate_coshelek():
    
    bitcoin = str(0.00000)
    litecoin = str(0.00000)
    new_data = data + f"""
💰 Баланс кошелька: ~0₽
Рубль: 0₽
Bitcoin: {bitcoin} BTC (~0₽)
Litecoin: {litecoin} LTC (~0₽)

☑️ Выберите кошелёк:"""
    return new_data