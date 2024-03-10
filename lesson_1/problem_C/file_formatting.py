SPACES_IN_TAB_COUNT = 4

# Нажатия клавиш для одной строки
def count_keystrokes_in_string(string_length):

    # Вычисляется максимально возможное количество табуляций и запоминается остаток
    keystrokes_count, unallocated_spaces_count = divmod(string_length, SPACES_IN_TAB_COUNT)

    # Если осталось 3 пробела, можно их заменить на одну табуляцию и один бэкспэйс
    if unallocated_spaces_count == 3:
        keystrokes_count += 2
    else:
        keystrokes_count += unallocated_spaces_count

    return keystrokes_count

def count_keystrokes(strings_lengths_list):
    keystrokes_count = 0
    for string_length in strings_lengths_list:
        keystrokes_count += count_keystrokes_in_string(string_length)

    return keystrokes_count

if __name__ == '__main__':
    strings_count = int(input())
    strings_lengths_list = [int(input()) for _ in range(strings_count)]

    print(count_keystrokes(strings_lengths_list))
