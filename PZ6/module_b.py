def process_data(value):

    if not isinstance(value, (int, float)):
        raise TypeError("Значение должно быть числом")
    
    if value < 0:
        raise ValueError("Значение не может быть отрицательным")
    

    return value * 2