def dfs_iterative(graph, start):
    visited = set()  # Set to keep track of visited vertices
    stack = [start]  # Initialize a stack with the starting vertex

    while stack:
        vertex = stack.pop()  # Pop a vertex from the stack
        if vertex not in visited:
            print(vertex, end=" ")  # Process the vertex
            visited.add(vertex)  # Mark the vertex as visited

            # Push all adjacent vertices onto the stack
            for neighbor in graph.graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set

    visited.add(vertex)  # Mark the vertex as visited
    print(vertex, end=" ")  # Process the vertex

    # Recur for all adjacent vertices
    for neighbor in graph.graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
