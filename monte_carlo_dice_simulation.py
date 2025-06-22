import random
import matplotlib.pyplot as plt

n = 100000
results = {i: 0 for i in range(2, 13)}

for _ in range(n):
    total = random.randint(1, 6) + random.randint(1, 6)
    results[total] += 1

monte_carlo_probs = {s: round(results[s] / n, 4) for s in results}

theoretical_probs = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

print("Сума | Монте-Карло | Теоретична")
for s in range(2, 13):
    print(f"{s:>4} | {monte_carlo_probs[s]*100:10.2f}% | {theoretical_probs[s]*100:10.2f}%")

x = list(range(2, 13))
mc_vals = [monte_carlo_probs[s] for s in x]
th_vals = [theoretical_probs[s] for s in x]

plt.bar(x, mc_vals, width=0.4, label='Монте-Карло', align='center')
plt.bar([i + 0.4 for i in x], th_vals, width=0.4, label='Теоретична', align='center')
plt.xlabel("Сума")
plt.ylabel("Ймовірність")
plt.title("Порівняння: Монте-Карло vs Теоретичні ймовірності")
plt.xticks([i + 0.2 for i in x], x)
plt.legend()
plt.grid(axis='y')
plt.show()
