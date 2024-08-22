"""
Работа бинарного поиска.
Немного теории: Бинарный поиск применяется только к отсортированным данным.
Работает по принципу сравнения искомого значения со среднем значением массива
данных.
"""

number_min = 1
number_max = 1024
numbers = [i for i in range(number_min, number_max + 1)]

search = {
    'launch_counter': 0,
    'user_number': False,
    'low_number': number_min,
    'high_number': number_max,
    'search_completed': False
}

text_ending = {1: ''}
text_ending.update({key: 'a' for key in [2, 3, 4]})
text_ending.update({key: 'ов' for key in [0, 5, 6, 7, 8, 9]})


def search_step(data: dict):
    search_number = (data['high_number'] - data['low_number']) // 2 +\
                         data['low_number']
    if search_number == data['user_number']:
        data['search_completed'] = True
    elif search_number < data['user_number']:
        data['low_number'] = search_number
    else:
        data['high_number'] = search_number
    data['launch_counter'] += 1
    return data


while True:
    search['user_number'] = int(input(f'Введите число от {number_min} '
                                      f'до {number_max}: '))
    if 0 < search['user_number'] < number_max + 1:
        break
    else:
        print('Не корректное значение. Попробуйте ещё раз.')

while True:
    search = search_step(search)
    # print(search)  # раскоментить для отладки
    if search['search_completed']:
        break

print(f'Число было определено за {search['launch_counter']} '
      f'шаг{text_ending[search['launch_counter'] % 10]}')
