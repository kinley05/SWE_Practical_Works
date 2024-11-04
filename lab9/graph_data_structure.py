from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()  # Initialize the visited set on first call
        visited.add(vertex)
        print(vertex, end=' ')  # Process the current vertex
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()  # Set to keep track of visited vertices
        queue = deque([start])  # Initialize the queue with the starting vertex
        visited.add(start)

        while queue:
            vertex = queue.popleft()  # Dequeue a vertex
            print(vertex, end=' ')  # Process the current vertex

            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark the neighbor as visited
                    queue.append(neighbor)  # Enqueue the neighbor

if __name__ == "__main__":
    g = Graph()
    # Manually adding edges based on your input
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    print("DFS starting from vertex 0:")
    g.dfs(0)  # Start DFS from vertex 0
    print("\nBFS starting from vertex 0:")
    g.bfs(0)  # Start BFS from vertex 0
