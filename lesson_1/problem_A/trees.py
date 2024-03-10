# Вычисляет кличество деревьем в одном интервале
def count_trees_in_section(start, end):
    return abs(end - start) + 1

def count_trees(P, V, Q, M):

    # Может покрасить первый
    P_start = P - V
    P_end = P + V
    P_count = count_trees_in_section(P_end, P_start)

    # Может покрасить второй
    Q_start = Q - M
    Q_end = Q + M
    Q_count = count_trees_in_section(Q_end, Q_start)

    # Количество общих дееревьев
    max_start = max(P_start, Q_start)
    min_end = min(P_end, Q_end)
    if max_start <= min_end:
        compensation = count_trees_in_section(min_end, max_start)
    else:
        compensation = 0

    # Из общего количества вычитаются общие деревья
    result = P_count + Q_count - compensation

    return result


if __name__ == '__main__':
    (P, V) = list(map(int, input().split()))
    (Q, M) = list(map(int, input().split()))

    trees_count = count_trees(P, V, Q, M)

    print(trees_count)
