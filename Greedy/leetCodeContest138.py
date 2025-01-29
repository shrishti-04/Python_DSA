# Find the minimum damage to kill the enemy
import math

def minDamageToKillEnemy(health, damage, power):
    n = len(health)
    threat = []

    for i in range(n):
        time_to_kill = math.ceil(health[i] / power)
        threat.append((time_to_kill / damage[i], i))

    threat.sort()
    cummulative_damage = sum(damage)
    total_damage = 0

    for i in range(n):
        idx = threat[i][1]
        time_to_kill = math.ceil(health[idx] / power)
        total_damage += cummulative_damage * time_to_kill
        cummulative_damage -= damage[idx]

    return total_damage

health = [3, 5, 7]
damage = [4, 6, 8]
power = 3
print(minDamageToKillEnemy(health, damage, power))