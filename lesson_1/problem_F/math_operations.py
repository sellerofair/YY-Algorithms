ADD_SYMBOL = '+'
MUL_SYMBOL = 'x'

# Проверяет, является ли число нечетным
def is_odd(number):
    return number % 2 == 1

# Считает количество нечетных чисел в списке
def count_odd_numbers(numbers_list):
    result = 0

    for number in numbers_list:
        if is_odd(number):
            result += 1

    return result

def find_operations(numbers_list):

    # Изначально определяем список операций, где все - сложение
    operations = [ADD_SYMBOL for _ in range(len(numbers_list) - 1)]

    # Если количество нечетных чисел четное
    odd_numbers_count = count_odd_numbers(numbers_list)
    if not is_odd(odd_numbers_count):

        # Между четным и нечетным числом нужно поставить знак умножить
        if is_odd(numbers_list[0]):
            operations[0] = MUL_SYMBOL
        else:
            for i in range(1, len(numbers_list)):
                if is_odd(numbers_list[i]):
                    operations[i - 1] = MUL_SYMBOL

                    break

    return ''.join(operations)

if __name__ == '__main__':
    numbers_count = int(input())
    numbers_list = list(map(int, input().split()))

    print(find_operations(numbers_list))
