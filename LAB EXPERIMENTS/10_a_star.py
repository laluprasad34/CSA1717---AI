# A* Search algorithm
import heapq

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1}
}
h = {"A": 4, "B": 3, "C": 1, "D": 0}

start, goal = "A", "D"
queue = [(h[start], 0, start)]
parent = {start: None}
cost = {start: 0}

while queue:
    f, g, node = heapq.heappop(queue)
    if node == goal:
        break
    for neighbour, weight in graph[node].items():
        new_cost = g + weight
        if new_cost < cost.get(neighbour, float("inf")):
            cost[neighbour] = new_cost
            parent[neighbour] = node
            heapq.heappush(queue, (new_cost + h[neighbour], new_cost, neighbour))

path = []
node = goal
while node is not None:
    path.append(node)
    node = parent.get(node)
path.reverse()
print("Path:", " -> ".join(path))
print("Total cost:", cost[goal])
