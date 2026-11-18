# Missionaries and Cannibals using BFS
from collections import deque

start = (3, 3, 0)  # left missionaries, left cannibals, boat (0=left, 1=right)
goal = (0, 0, 1)
moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

def safe(m, c):
    rm, rc = 3-m, 3-c
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (rm == 0 or rm >= rc)

queue = deque([start])
parent = {start: None}

while queue:
    m, c, boat = queue.popleft()
    if (m, c, boat) == goal:
        break
    for dm, dc in moves:
        if boat == 0:
            nxt = (m-dm, c-dc, 1)
        else:
            nxt = (m+dm, c+dc, 0)
        if safe(nxt[0], nxt[1]) and nxt not in parent:
            parent[nxt] = (m, c, boat)
            queue.append(nxt)

path = []
state = goal
while state is not None:
    path.append(state)
    state = parent.get(state)
for state in reversed(path):
    print("Left bank:", state[0], "missionaries,", state[1], "cannibals; Boat:", state[2])
