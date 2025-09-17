from module_a import call_processing

if __name__ == "__main__":
    test_values = [5, -2, "text", 10.5]
    
    for value in test_values:
        print(f"\nТестируем значение: {value}")
        result = call_processing(value)
        if result is not None:
            print(f"Успешно: {result}")