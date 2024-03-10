# n - изначальная прибыль
# k - количество учредителей компании
# d - количество дней, которое нужно следить за прибылью

# Перебирать каждый день нет смысла
# Если после первого дня прибыль делится на k,
# То достаточно добавлять в конец нули
import sys


def calculate_profit(n, k, d):
    profit = n
    new_profit = profit * 10
    success = False
    for i in range(10):
        profit = new_profit + i
        if profit % k == 0:
            success = True
            break

    if not success:
        return -1

    profit = profit * (10 ** (d - 1))

    return profit

if __name__ == '__main__':
    (n, k, d) = list(map(int, input().split()))

    # Увеличение ограничения на длину чисел для преобразования в строку
    # Иначе будет ошибка
    # ValueError: Exceeds the limit (4300 digits) for integer string conversion
    sys.set_int_max_str_digits(1000000)

    print(calculate_profit(n, k, d))
