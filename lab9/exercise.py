def bfs_shortest_path(self, start, goal):
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()
        
        if vertex == goal:
            return path  
        
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  

def has_cycle(self):
    visited = set()
    
    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif parent != neighbor:  
                return True
        return False

    for v in self.graph:
        if v not in visited:  
            if dfs(v, None):
                return True
    return False

import heapq

def dijkstra(self, start, goal):
    distances = {vertex: float('infinity') for vertex in self.graph}
    distances[start] = 0
    priority_queue = [(0, start)]  

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in self.graph.get(current_vertex, []):
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances.get(goal, float('infinity'))  

def is_bipartite(self):
    color = {}
    
    def bfs(vertex):
        queue = deque([vertex])
        color[vertex] = 0  
        
        while queue:
            v = queue.popleft()
            for neighbor in self.graph.get(v, []):
                if neighbor not in color:
                    color[neighbor] = 1 - color[v] 
                    queue.append(neighbor)
                elif color[neighbor] == color[v]:  
                    return False
        return True

    for v in self.graph:
        if v not in color:  
            if not bfs(v):
                return False
    return True

from collections import deque
import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  

    def bfs_shortest_path(self, start, goal):
        visited = {start}
        queue = deque([(start, [start])])  

        while queue:
            vertex, path = queue.popleft()
            
            if vertex == goal:
                return path
            
            for neighbor in self.graph.get(vertex, []):
                if neighbor[0] not in visited:  
                    visited.add(neighbor[0])
                    queue.append((neighbor[0], path + [neighbor[0]]))
        
        return None

    def has_cycle(self):
        visited = set()
        
        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor in self.graph.get(vertex, []):
                if neighbor[0] not in visited:  
                    if dfs(neighbor[0], vertex):
                        return True
                elif parent != neighbor[0]:  
                    return True
            return False

        for v in self.graph:
            if v not in visited:  
                if dfs(v, None):
                    return True
        return False

    def dijkstra(self, start, goal):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances.get(goal, float('infinity'))

    def is_bipartite(self):
        color = {}
        
        def bfs(vertex):
            queue = deque([vertex])
            color[vertex] = 0  
            
            while queue:
                v = queue.popleft()
                for neighbor, _ in self.graph.get(v, []):
                    if neighbor not in color:
                        color[neighbor] = 1 - color[v]
                        queue.append(neighbor)
                    elif color[neighbor] == color[v]:  
                        return False
            return True

        for v in self.graph:
            if v not in color:  
                if not bfs(v):
                    return False
        return True


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    
    print("Shortest path from 0 to 3:", g.bfs_shortest_path(0, 3))
    print("Graph has a cycle:", g.has_cycle())
    
    g2 = Graph()
    g2.add_edge(0, 1, 1)
    g2.add_edge(1, 2, 2)
    g2.add_edge(0, 2, 2)
    g2.add_edge(1, 3, 1)
    
    print("Shortest distance from 0 to 3:", g2.dijkstra(0, 3))
    
    g3 = Graph()
    g3.add_edge(0, 1)
    g3.add_edge(0, 3)
    g3.add_edge(1, 2)
    g3.add_edge(2, 3)
    
    print("Graph is bipartite:", g3.is_bipartite())
