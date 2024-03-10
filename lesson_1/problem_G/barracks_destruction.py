# x - количество солдат на старте игры
# y - количество очков здоровья казармы
# p - количество производимых за раунд казармой солдат

# По максимуму урон на бараки
# Остальное на воинов в бараках
def attack_barracks_health(attackers_power, barracks_health, barracks_power):
    remained_power = max(attackers_power - barracks_health, 0)
    barracks_health -= attackers_power - remained_power
    barracks_power -= remained_power

    return barracks_health, barracks_power

# Уничтожаются все воины в бараках
# Остальные воины атакуют бараки
def attack_barracks_power(attackers_power, barracks_health, barracks_power):
    barracks_health -= attackers_power - barracks_power

    return barracks_health, 0


def destruct_barracks(attackers_power, barracks_health, barracks_productivity):
    attackers_start_power = attackers_power
    barracks_start_health = barracks_health
    barracks_power = 0

    # Выбор стратегии
    if attackers_power > barracks_productivity:
        attac_barracks = attack_barracks_power
    else:
        attac_barracks = attack_barracks_health

    rounds_count = 0
    while barracks_health > 0 or barracks_power > 0:
        rounds_count += 1

        print(attackers_power, barracks_health, barracks_power)

        # Ход нападающих
        barracks_health, barracks_power = attac_barracks(attackers_power, barracks_health, barracks_power)

        # Ход казармы
        attackers_power -= barracks_power
        if attackers_power <= 0:
            return -1

        # Производство воинов казармой
        if barracks_health > 0:
            barracks_power += barracks_productivity

    return rounds_count

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    p = int(input())

    print(destruct_barracks(x, y, p))
