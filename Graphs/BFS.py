from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited vertices
    queue = deque([start])  # Initialize a queue with the starting vertex

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        if vertex not in visited:
            print(vertex, end=" ")  # Process the vertex
            visited.add(vertex)  # Mark the vertex as visited

            # Enqueue all adjacent vertices that haven't been visited
            for neighbor in graph.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
