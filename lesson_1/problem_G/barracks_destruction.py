# x - количество солдат на старте игры
# y - количество очков здоровья казармы
# p - количество производимых за раунд казармой солдат

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

def attack_barracks(game_state):
    attackers_power = game_state['attackers_power']
    barracks_health = game_state['barracks_health']
    barracks_productivity = game_state['barracks_productivity']
    barracks_power = game_state['barracks_power']

    # Если сила атакующих не больше, чем производят бараки,
    # Шанс только по-максимуму бить казармы
    if attackers_power <= barracks_productivity:
        attack_barracks_health(game_state)
        return

    # Расчет возможности уничтожить казармы
    barracks_destruction_available = False
    if 0 < barracks_health < attackers_power:
        remained_power = attackers_power - barracks_health
        remained_barracks_power = barracks_power - remained_power
        barracks_destruction_available = attackers_power >= remained_barracks_power * 2

    if barracks_destruction_available:
        attack_barracks_health(game_state)
    else:
        attack_barracks_power(game_state)

def destruct_barracks(attackers_power, barracks_health, barracks_productivity):
    game_state = {
        'attackers_power': attackers_power,
        'barracks_health': barracks_health,
        'barracks_productivity': barracks_productivity,
        'barracks_power': 0
    }

    rounds_count = 0
    while game_state['barracks_health'] > 0 or game_state['barracks_power'] > 0:
        rounds_count += 1

        # Ход нападающих
        attack_barracks(game_state)

        # Ход казармы
        game_state['attackers_power'] -= game_state['barracks_power']
        if game_state['attackers_power'] <= 0:
            return -1

        # Производство воинов казармой
        if game_state['barracks_health'] > 0:
            game_state['barracks_power'] += game_state['barracks_productivity']

    return rounds_count

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    p = int(input())

    print(destruct_barracks(x, y, p))
