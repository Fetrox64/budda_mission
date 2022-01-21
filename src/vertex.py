class Vertex:
    def __init__(self, v: list[str]):
        self.id = v[0]
        self.name = v[1]
        self.route = v[2]
        self.visited = False
        self.level = -1
        self.neighbor_set = []

    def add_neighbor(self, n):
        if n not in self.neighbor_set:
            self.neighbor_set.append(n)
