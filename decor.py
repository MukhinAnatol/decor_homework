#Написать декоратор - логгер. Он записывает в файл:
# дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

#Написать декоратор из п.1, но с параметром – путь к логам.

#Применить написанный логгер к приложению из любого предыдущего д/з.

from datetime import datetime
import os

my_path = os.getcwd()


def logger(path):
    def _logger(old_function):
        def new_function(*args):
            start = datetime.now()
            result = old_function(*args)
            pass
            with open(path + r'\log.txt', 'w', encoding='utf-8') as file:
                file.write(f'{start}\n {old_function.__name__}\n {args} \n {result}')
            return result

        return new_function

    return _logger


@logger(my_path)
def get_recipes(file_name: str):
    cook_book = {}
    with open(file_name, 'rt', encoding = 'utf-8') as file:
        for line in file:
            if '|' not in line and len(line) > 2:
                dish = line.split('\n')[0]
                cook_book[dish] = []
                quantity = int(file.readline())
                for ingr in range(quantity):
                    ingr = file.readline().split(' | ')
                    cook_book[dish].append({'ingredient_name': ingr[0],
                                            'quantity': int(ingr[1]),
                                           'measure': ingr[2].replace('\n', '')})
    return cook_book

recipe = 'cook_book.txt'
get_recipes(recipe)