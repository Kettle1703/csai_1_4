from collections import Counter


def count_common_elements(*lists):
    if not lists:
        return 0

    # Список словарей для подсчета количества каждого элемента по списку
    element_counters = [Counter(lst) for lst in lists]

    # Множество для взятия пересечения элементов по спискам
    common_elements = set().union(*[el.elements() for el in element_counters])

    # Удаление повторений элементов из множества
    common_count = {
        element: min(element_counters[i][element] for i in range(len(element_counters)))
        for element in common_elements
    }

    # Общая сумма значений данного множества
    total_count = sum(common_count.values())
    return total_count


if __name__ == '__main__':
    n = int(input('\nВведите количество списков: '))
    plenty = []

    for j in range(n):  # Ввод списков
        user_input = input(f'Введите элементы списка {j + 1}, разделенные пробелами: ')
        plenty.append(list(map(int, user_input.split())))

    result = count_common_elements(*plenty)
    print(f'Количество одинаковых элементов во всех списках: {result}')
