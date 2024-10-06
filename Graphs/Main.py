from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []  # Create a list for the vertex u if it doesn't exist
        if v not in self.graph:
            self.graph[v] = []  # Create a list for the vertex v if it doesn't exist
        self.graph[u].append(v)  # Add v to the adjacency list of u
        # For undirected graph, uncomment the next line:
        # self.graph[v].append(u)  # Add u to the adjacency list of v

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

# Example usage of the Graph class and BFS/DFS functions
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)

    print("BFS starting from vertex 0:")
    bfs(g, 0)
    print("\nDFS (Iterative) starting from vertex 0:")
    dfs_iterative(g, 0)
    print("\nDFS (Recursive) starting from vertex 0:")
    dfs_recursive(g, 0)
