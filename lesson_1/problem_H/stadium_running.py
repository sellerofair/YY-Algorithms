def run_around_stadium(L, X1, V1, X2, V2):
    answer_exists = False
    time_to_equal_distance = 0

    return answer_exists, time_to_equal_distance


if __name__ == '__main__':
    (L, X1, V1, X2, V2) = list(map(int, input().split()))

    answer_exists, time_to_equal_distance = run_around_stadium(L, X1, V1, X2, V2)

    if answer_exists:
        print('yes')
        print(time_to_equal_distance)
    else:
        print('no')
