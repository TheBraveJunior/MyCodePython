"""
Работа бинарного поиска.
"""

number_min = 1
number_max = 100
numbers = [i for i in range(number_min, number_max + 1)]
user_number = 0


def search_number(min_number, max_number):
    i = 1
    search = tuple()

    if max_number // 2 == user_number:
        print('Ваше число: ', max_number // 2)
        return i
    elif max_number // 2 < user_number:
        search = (max_number // 2, max_number)
    else:
        search = (min_number, max_number // 2)

    while True:
        i += 1
        next_search_number = (search[1] - search[0]) // 2 + search[0]
        if next_search_number == user_number:
            print('Ваше число: ', next_search_number)
            break
        elif next_search_number < user_number:
            search = (next_search_number, search[1])
        else:
            search = (search[0], next_search_number)
    return i


while True:
    user_number = int(input(f'Введите число от {number_min} до {number_max}: '))
    if 0 < user_number < number_max + 1:
        break
    else:
        print('Не корректное значение. Попробуйте ещё раз.')

i = search_number(number_min, number_max)

text_ending = {1: ''}
text_ending.update({key: 'a' for key in [2, 3, 4]})
text_ending.update({key: 'ов' for key in [0, 5, 6, 7, 8, 9]})

print(f'Число было определено за {i} шаг{text_ending[i % 10]}')
