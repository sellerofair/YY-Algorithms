# x - количество солдат на старте игры
# y - количество очков здоровья казармы
# p - количество производимых за раунд казармой солдат

from math import sqrt


# Золотое сечение
GOLDEN_RATIO = (1 + sqrt(5)) / 2


# По максимуму урон на бараки
# Остальное на воинов в бараках
def attack_barracks_health(game_state):
    attackers_power = game_state['attackers_power']

    remained_power = max(attackers_power - game_state['barracks_health'], 0)
    game_state['barracks_health'] -= attackers_power - remained_power
    game_state['barracks_power'] -= remained_power

# По максимуму урон на воинов в бараках
# Остальное на бараки
def attack_barracks_power(game_state):
    attackers_power = game_state['attackers_power']

    remained_power = max(attackers_power - game_state['barracks_power'], 0)
    game_state['barracks_power'] -= attackers_power - remained_power
    game_state['barracks_health'] -= remained_power

def select_attackers_move(game_state):
    attackers_power = game_state['attackers_power']
    barracks_health = game_state['barracks_health']
    barracks_productivity = game_state['barracks_productivity']
    barracks_power = game_state['barracks_power']

    # Если сила атакующих не больше, чем производят бараки,
    # Шанс только по-максимуму бить казармы
    if attackers_power <= barracks_productivity:
        return attack_barracks_health

    # Расчет возможности уничтожить казармы
    if 0 < barracks_health <= attackers_power:
        pass

        # FIXME: It doesn't work on Test 7
        # remained_power = attackers_power - barracks_health
        # remained_barracks_power = barracks_power - remained_power
        # barracks_destruction_available = attackers_power >= remained_barracks_power * 2
        # if barracks_destruction_available:
        #     return attack_barracks_health

        # FIXME: It doesn't work on Test 5
        # powers_ratio = (barracks_health + barracks_power) / attackers_power
        # if powers_ratio < GOLDEN_RATIO:
        #     return attack_barracks_health

    return attack_barracks_power

def make_move(game_state):
    game_state['moves_count'] += 1

    print(game_state)
    
    # Ход атакующих
    attackers_move = select_attackers_move(game_state)
    print(attackers_move.__name__)
    attackers_move(game_state)

    # Ход казармы
    game_state['attackers_power'] -= game_state['barracks_power']

    # Производство воинов казармой
    if game_state['barracks_health'] > 0:
        game_state['barracks_power'] += game_state['barracks_productivity']

def destruct_barracks(attackers_power, barracks_health, barracks_productivity):
    if barracks_health < attackers_power:
        return 1

    # Состояние игры
    game_state = {
        'attackers_power': attackers_power,
        'barracks_health': barracks_health,
        'barracks_productivity': barracks_productivity,
        'barracks_power': 0,
        'moves_count': 0
    }

    while game_state['barracks_health'] > 0 or game_state['barracks_power'] > 0:
        make_move(game_state)

        if game_state['attackers_power'] <= 0:
            return -1

    return game_state['moves_count']

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    p = int(input())

    print(destruct_barracks(x, y, p))
