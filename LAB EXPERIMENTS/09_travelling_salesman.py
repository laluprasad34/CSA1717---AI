# Travelling Salesman Problem (simple brute force)
from itertools import permutations

cities = ["A", "B", "C", "D"]
distance = {
    "A": {"A":0, "B":10, "C":15, "D":20},
    "B": {"A":10, "B":0, "C":35, "D":25},
    "C": {"A":15, "B":35, "C":0, "D":30},
    "D": {"A":20, "B":25, "C":30, "D":0}
}

best_cost = float("inf")
best_route = None

for order in permutations(cities[1:]):
    route = ["A"] + list(order) + ["A"]
    cost = 0
    for i in range(len(route)-1):
        cost += distance[route[i]][route[i+1]]
    if cost < best_cost:
        best_cost = cost
        best_route = route

print("Best route:", " -> ".join(best_route))
print("Minimum cost:", best_cost)
