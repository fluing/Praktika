import random

# Функция для подбрасывания монеты
def podbros_monety():
    return random.choice(["Орёл", "Решка"])

# Симуляция подбрасывания монеты
result = podbros_monety()
print(f"Результат подбрасывания: {result}")