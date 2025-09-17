from module_b import process_data

def call_processing(value):

    try:
        result = process_data(value)
        print(f"Обработанное значение: {result}")
        return result
    except (TypeError, ValueError) as e:
        print(f"Ошибка обработки: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None