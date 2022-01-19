from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertex_set = {}

    def addVertex(self, v: list[str]):
        identifier = v[0]
        if identifier not in self.vertex_set:
            self.vertex_set[identifier] = Vertex(v)

    def addEdge(self, v: list[str]):
        vertex_a = self.vertex_set[v[0]]
        vertex_b = self.vertex_set[v[1]]
        vertex_b.addNeighbor(vertex_a)
        vertex_a.addNeighbor(vertex_b)
