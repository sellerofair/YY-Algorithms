def count_goals_for_victory(first_game_score, current_score, first_game_owner):

    # Получение счета в числах
    (first_game_friend_score, first_game_enemy_score) = list(map(int, first_game_score.split(':')))
    (current_game_friend_score, current_game_enemy_score) = list(map(int, current_score.split(':')))
    first_game_owner = int(first_game_owner)

    # Вычисление форы
    first_game_handicap = first_game_friend_score - first_game_enemy_score
    current_game_handicap = current_game_friend_score - current_game_enemy_score

    # Если общая фора больше нуля, уже победа, голы не нужны
    total_handicap = first_game_handicap + current_game_handicap
    if total_handicap > 0:
        return 0

    # Количество голов для ничьей
    goals_to_draw = total_handicap * -1

    # Вычисление преимущества по голам в гостях
    if first_game_owner == 1:
        away_goals_advantage = (current_game_friend_score + goals_to_draw) - first_game_enemy_score
    else:
        away_goals_advantage = first_game_friend_score - current_game_enemy_score

    # Если есть преимущество по голам в гостях, достаточно ничьей
    # Если нет, нужна только победа и добавляется один гол
    result = goals_to_draw
    if away_goals_advantage <= 0:
        result += 1

    return result

if __name__ == '__main__':
    print(count_goals_for_victory(input(), input(), input()))
