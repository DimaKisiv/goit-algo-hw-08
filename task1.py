import heapq
import random

operations_cost = 0
cables = [random.randint(1, 10) for _ in range(10)]
print(f"Довжини кабелів: {cables}")
#перетворюємо довжини кабелів в купу щоб з неї брати завжди найкоротші елементи
heapq.heapify(cables)
while len(cables) > 1:
    #беремо найкоротші елементи з купи
    shortest_cable1 = heapq.heappop(cables)
    shortest_cable2 = heapq.heappop(cables)
    #обєднуємо їх та додаємо до загальної ціни операцій
    merged_cable = shortest_cable1 + shortest_cable2
    operations_cost += merged_cable
    #додаємо обєднаний кабель знову для продовження обєднання
    heapq.heappush(cables, merged_cable)
    print(f"Взято 2 найкоротші кабелі: {shortest_cable1}, {shortest_cable2}")
    print(f"Додано до решти кабелів обєднані з довжиною: {merged_cable}")


print(f"Ціна всіх операцій: {operations_cost}")
print(f"Кінцева довжина кабеля: {cables[0]}")
