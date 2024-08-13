def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print("1.Функция с параметрами по умолчанию:")
print_params()
print_params(b = 25)
print_params(c=[1,2,3])
print("2.Распаковка параметров:")
values_list = [1, True, "Два"]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)
print("3.Распаковка + отдельные параметры:")
values_list_2 = ["'Три'", False]
print_params(42, *values_list_2) # Поменял местами для проверки