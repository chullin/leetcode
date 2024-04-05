from collections import deque

queue = deque([1, 2, 3, 4, 5])
# print(queue)

while queue:
    print(queue)
    queue.popleft()