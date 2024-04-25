class Graph:
    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.incidence_matrix = [[0] * num_edges for _ in range(num_vertices)]

    def add_edge(self, edge_index, vertices):
        for vertex_index in vertices:
            self.incidence_matrix[vertex_index][edge_index] = 1

    def remove_edge(self, edge_index, vertices):
        for vertex_index in vertices:
            self.incidence_matrix[vertex_index][edge_index] = 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.incidence_matrix])


# Example usage:
if __name__ == "__main__":
    num_vertices = 4
    num_edges = 5
    graph = Graph(num_vertices, num_edges)
    graph.add_edge(0, [0, 1])
    graph.add_edge(1, [0, 2])
    graph.add_edge(2, [1, 2])
    graph.add_edge(3, [2, 3])
    graph.add_edge(4, [0, 3])

    print("Incidence Matrix:")
    print(graph)
