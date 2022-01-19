class Vertex:
    def __init__(self, v: list[str]):
        self.id = v[0]
        self.name = v[1]
        self.route = v[2]
        self.neighbor_set = []

    def addNeighbor(self, n):
        if n not in self.neighbor_set:
            self.neighbor_set.append(n)
