def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
    return result, incorrect_data

def calculate_average(numbers):
    if not isinstance(numbers, (list, str, tuple, set)):
        print('В numbers записан некорректный тип данных')
        return None
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data
        return total_sum / count if count > 0 else 0
    except ZeroDivisionError:
        return 0

# Пример вызовов:
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Результат 1: 0
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Результат 2: 2.0
print(f'Результат 3: {calculate_average(567)}')  # Результат 3: None
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Результат 4: 26.5
