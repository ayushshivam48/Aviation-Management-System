class Graph:
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []
            print(f"Vertex {vertex} added.")

    def add_edge(self, vertex1, vertex2):
        """Add an edge between vertex1 and vertex2 (undirected graph)."""
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
        print(f"Edge added between {vertex1} and {vertex2}.")

    def display(self):
        """Display the adjacency list representation of the graph."""
        for vertex in self.graph:
            print(f"{vertex}: {', '.join(self.graph[vertex])}")

    def bfs(self, start_vertex):
        """Perform Breadth-First Search (BFS) from the start_vertex."""
        visited = set()
        queue = [start_vertex]
        print(f"BFS starting from vertex {start_vertex}:")

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=" ")

                # Add unvisited neighbors to the queue
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()  # New line after BFS output

    def dfs(self, start_vertex, visited=None):
        """Perform Depth-First Search (DFS) from the start_vertex."""
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=" ")

        # Visit all the neighbors of the current vertex
        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage
if __name__ == "__main__":
    g = Graph()
    
    # Add vertices
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')

    # Add edges
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')

    # Display the graph
    g.display()

    # Perform BFS and DFS
    g.bfs('A')  # Starting BFS from vertex A
    print("DFS starting from vertex A:")
    g.dfs('A')  # Starting DFS from vertex A
