def count_goals_for_victory(first_game_score, current_score, first_game_owner):
    (first_game_friend_score, first_game_enemy_score) = list(map(int, first_game_score.split(':')))
    (current_game_friend_score, current_game_enemy_score) = list(map(int, current_score.split(':')))

    first_game_handicap = first_game_friend_score - first_game_enemy_score
    current_game_handicap = current_game_friend_score - current_game_enemy_score

    total_handicap = first_game_handicap + current_game_handicap
    if total_handicap > 0:
        return 0

    goals_to_draw = total_handicap * -1
    result = goals_to_draw + 1

    if first_game_owner == '1':
        away_goals_advantage = (current_game_friend_score + goals_to_draw) - first_game_enemy_score
    else:
        away_goals_advantage = first_game_friend_score - current_game_enemy_score

    if away_goals_advantage > 0:
        result -= 1

    return result

if __name__ == '__main__':
    print(count_goals_for_victory(input(), input(), input()))
