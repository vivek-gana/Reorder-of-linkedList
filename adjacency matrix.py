class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, v1, v2,weight):
        # Assuming undirected graph
        self.adj_matrix[v1][v2] = weight
        self.adj_matrix[v2][v1] = weight

    def remove_edge(self, v1, v2):
        # Assuming undirected graph
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.adj_matrix])


# Example usage:
if __name__ == "__main__":
    num_vertices = 5
    graph = Graph(num_vertices)
    graph.add_edge(0, 1,3)
    graph.add_edge(1,2,5)
    graph.add_edge(3,4,6)
    graph.add_edge(0,4,7)
    graph.add_edge(4,1,11)
    graph.add_edge(1,3,2)
    graph.add_edge(2,3,10)
    
    print("Adjacency Matrix:")
    print(graph)
