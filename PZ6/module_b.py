def process_data(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Значение должно быть числом")
    
    if value < 0:
        raise ValueError("Значение не может быть отрицательным")
    
    if value == 5:  # ошибка
        return value / 0
    
    return value * 2