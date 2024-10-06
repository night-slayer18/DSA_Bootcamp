# Adjacency List
# An adjacency list can be implemented using a dictionary in Python.

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
