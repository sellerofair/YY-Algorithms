# Везде i - номер строки
#       j - номер столбца

ROWS_COUNT = 8
COLS_COUNT = 8

MODIFIED_ROWS_COUNT = ROWS_COUNT + 2
MODIFIED_COLS_COUNT = COLS_COUNT + 2

# Проверяет, свободна ли ячейка
# Ячейка, обозначающая границу не свободна
def is_free_cage(chessboard, i, j):
    return chessboard[i][j] == '*'

# i, j - координаты фигуры
def apply_rook_beats(chessboard, safe_cages_chessboard, i, j):

    # По горизонтали
    def apply_h_beats(shift):
        shifted_j = j + shift
        while is_free_cage(chessboard, i, shifted_j):
            safe_cages_chessboard[i][shifted_j] = 0
            shifted_j += shift

    # По вертикали
    def apply_v_beats(shift):
        shifted_i = i + shift
        while is_free_cage(chessboard, shifted_i, j):
            safe_cages_chessboard[shifted_i][j] = 0
            shifted_i += shift

    # Отметка на ячейке с фигурой
    safe_cages_chessboard[i][j] = 0

    # Ходы
    apply_h_beats(-1)
    apply_h_beats(1)
    apply_v_beats(-1)
    apply_v_beats(1)

# i, j - координаты фигуры
def apply_bishop_beats(chessboard, safe_cages_chessboard, i, j):

    def apply_beats(i_shift, j_shift):
        shifted_i = i + i_shift
        shifted_j = j + j_shift
        while is_free_cage(chessboard, shifted_i, shifted_j):
            safe_cages_chessboard[shifted_i][shifted_j] = 0
            shifted_i += i_shift
            shifted_j += j_shift

    # Отметка на ячейке с фигурой
    safe_cages_chessboard[i][j] = 0

    # Ходы
    apply_beats(-1, -1)
    apply_beats(1, 1)
    apply_beats(1, -1)
    apply_beats(-1, 1)

def count_safe_cages(chessboard):

    # Создается модифицированная доска с фигурами
    # Добавляются границы, для исключения выхода за пределы
    modified_chessboard = ['+' * MODIFIED_COLS_COUNT]
    for row in chessboard:
        modified_chessboard.append('+' + row + '+')
    modified_chessboard.append('+' * MODIFIED_COLS_COUNT)

    # Дополнительное поле, где ячейки имеют значения:
    #  - 0 - ячейка занята или бьется одной из фигур
    #  - 1 - свободная не бьющаяся ячейка
    # Изначально заполняется единицами
    # Границы заполняются нулями
    safe_cages_chessboard = [[0 for _ in range(MODIFIED_COLS_COUNT)]]
    for _ in range(ROWS_COUNT):
        safe_cages_chessboard.append([0] + [1 for _ in range(COLS_COUNT)] + [0])
    safe_cages_chessboard.append([0 for _ in range(MODIFIED_COLS_COUNT)])

    # Ходы фигурами и отмечание битых клеток
    for i in range(MODIFIED_ROWS_COUNT):
        for j in range(MODIFIED_COLS_COUNT):
            if modified_chessboard[i][j] == 'B':
                apply_bishop_beats(modified_chessboard, safe_cages_chessboard, i, j)
            elif modified_chessboard[i][j] == 'R':
                apply_rook_beats(modified_chessboard, safe_cages_chessboard, i, j)

    return sum(map(sum, safe_cages_chessboard))

if __name__ == '__main__':
    chessboard = [input()[:COLS_COUNT] for _ in range(ROWS_COUNT)]

    print(count_safe_cages(chessboard))
