items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    efficiency = []
    for name, data in items.items():
        ratio = data["calories"] / data["cost"]
        efficiency.append((ratio, name, data))
    
    efficiency.sort(reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for ratio, name, data in efficiency:
        if total_cost + data["cost"] <= budget:
            selected_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost = data["cost"]
        calories = data["calories"]
        
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]
    
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name, data = item_list[i - 1]
            selected_items.append(name)
            w -= data["cost"]
    
    selected_items.reverse()
    
    total_cost = sum(items[item]["cost"] for item in selected_items)
    total_calories = sum(items[item]["calories"] for item in selected_items)
    
    return selected_items, total_cost, total_calories

budget = int(input("Введіть ваш бюджет: "))

print("Жадібний алгоритм:")
greedy_result = greedy_algorithm(items, budget)
print(f"Вибрані страви: {greedy_result[0]}")
print(f"Загальна вартість: {greedy_result[1]}")
print(f"Загальна калорійність: {greedy_result[2]}")

print("\nДинамічне програмування:")
dp_result = dynamic_programming(items, budget)
print(f"Вибрані страви: {dp_result[0]}")
print(f"Загальна вартість: {dp_result[1]}")
print(f"Загальна калорійність: {dp_result[2]}")

print(f"\nЕфективність калорій/вартість для кожної страви:")
for name, data in items.items():
    ratio = data["calories"] / data["cost"]
    print(f"{name}: {ratio:.2f} кал/грн")