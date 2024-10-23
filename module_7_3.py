import string

class WordsFinder:
    def __init__(self, *file_names):
        # При создании объекта класса сохраняем имена файлов в атрибут file_names
        self.file_names = file_names

    def get_all_words(self):
        # Создаём пустой словарь для хранения слов из файлов
        all_words = {}
        # Определяем список символов пунктуации, которые нужно удалить из текста
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        # Перебираем все файлы
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                # Читаем содержимое файла и переводим его в нижний регистр
                content = file.read().lower()
                # Удаляем пунктуацию из содержимого файла
                for p in punctuation:
                    content = content.replace(p, ' ')
                # Разбиваем строку на список слов
                words = content.split()
                # Записываем слова в словарь, где ключом будет имя файла
                all_words[file_name] = words

        return all_words

    def find(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        # Переводим искомое слово в нижний регистр для сравнения
        word = word.lower()
        # Создаём словарь для хранения результата
        result = {}

        # Перебираем имена файлов и слова в них
        for file_name, words in all_words.items():
            try:
                # Пытаемся найти первое вхождение слова и записываем его позицию (1-индексация)
                position = words.index(word) + 1
                result[file_name] = position
            except ValueError:
                # Если слово не найдено, записываем None
                result[file_name] = None

        return result

    def count(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        # Переводим искомое слово в нижний регистр
        word = word.lower()
        # Создаём словарь для хранения результата
        result = {}

        # Перебираем имена файлов и слова в них
        for file_name, words in all_words.items():
            # Считаем количество вхождений искомого слова в списке слов
            count = words.count(word)
            result[file_name] = count

        return result

# Пример использования класса:
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Получаем все слова из файлов
print(finder.find('text'))     # Ищем позицию первого вхождения слова "text"
print(finder.count('text'))    # Считаем количество вхождений слова "text"
