
my_dict = {"Имя": "Станислав", "Фамилия": "Алёхин", "Год Рождения": 1998}
print(my_dict)
print(my_dict["Имя"])
print(my_dict.get("Отчество"))
print(my_dict)
my_dict.update({"Город": "Рязань",
                "Телефон": 88005553535})
print(my_dict)
del my_dict["Имя"]
print(my_dict.get("Имя"))
print(my_dict)

my_set = {1, 2, 3, 1, "Phyton", False, 2, (1, 2, 3)}
print(my_set)
my_set.update([4, 6])
print(my_set)
my_set.discard("Phyton")
print(my_set)


