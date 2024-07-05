def names_clear(names_file: str) -> list:
    """Функция для очистки имен от пробелов и символов"""
    new_names_list = list()
    with open('data/' + names_file) as file_name:
        list_name = file_name.read().split()
        for name in list_name:
            new_name = ''
            for symbol in name:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_names_list.append(new_name)

    return new_names_list


if __name__ == '__names2sort__':
    cleared_names = names_clear('names.txt')
    for i in cleared_names:
        print(i)
