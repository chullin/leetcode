from collections import deque

def BFS(graph, start):
    visted = set()          # Set to keep track of visited nodes.
    queue = deque([start])  # 設定一個預設值有 start 的 queue
    visted.add(start)       # 將 start 加入 visited

    while queue:
        node = queue.popleft()  # 從 queue 最左邊取出
        print(node, end=" ")

        for neighbor in graph[node]:    # 當前節點的所有鄰居節點
            if neighbor not in visted:  # 如果鄰居節點還沒被 visited 過
                queue.append(neighbor)
                visted.add(neighbor)

# 圖表連接圖
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal starting from node A:")
BFS(graph, 'A')