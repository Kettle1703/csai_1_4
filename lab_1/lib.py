def count_common_elements(*lists):
    if not lists:
        return 0
    common_elements = set(lists[0])  # Используем множество для отслеживания общих элементов
    for lst in lists[1:]:  # Пересекаем множества с остальными списками
        common_elements.intersection_update(lst)
    return len(common_elements)


if __name__ == '__main__':
    n = int(input('\nВведите количество списков: '))
    plenty = []
    
    for i in range(n):  # Ввод списков
        user_input = input(f'Введите элементы списка {i + 1}, разделенные пробелами: ')
        plenty.append(list(map(int, user_input.split())))
    
    result = count_common_elements(*plenty)
    print(f'Количество одинаковых элементов во всех списках: {result}')
