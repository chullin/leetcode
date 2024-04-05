def DFS(graph, start):
    visited = set()  # Set to keep track of visited nodes.
    stack = [start]  # 設定一個預設值有 start 的 stack

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS traversal starting from node A:")
DFS(graph, 'A')