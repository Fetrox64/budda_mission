from logger import logger
from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertex_set = {}

    def add_vertex(self, v: list[str]):
        identifier = v[0]
        if identifier not in self.vertex_set:
            self.vertex_set[identifier] = Vertex(v)

    def add_edge(self, v: list[str]):
        vertex_a = self.vertex_set[v[0]]
        vertex_b = self.vertex_set[v[1]]
        vertex_b.add_neighbor(vertex_a)
        vertex_a.add_neighbor(vertex_b)

    def bfs(self, initial_node: Vertex, end_node: Vertex, route: str):
        print("===================================================================")
        logger('Starting search...')
        i = initial_node.id
        e = end_node.id

        if i in self.vertex_set and e in self.vertex_set:
            bfs_data = []
            queue = [i]
            self.vertex_set[i].visited = True
            self.vertex_set[i].level = 0
            bfs_data.append([i, str(self.vertex_set[i].level)])

            while len(queue) > 0:
                current = queue[0]
                queue = queue[1:]

                for v in self.vertex_set[current].neighbor_set:
                    v = v.id

                    if self.vertex_set[v].visited == False:
                        queue.append(v)
                        self.vertex_set[v].visited = True
                        self.vertex_set[v].level = self.vertex_set[current].level + 1

                        id = str(v)
                        level = str(self.vertex_set[v].level)
                        bfs_data.append([id, level])

            return bfs_data

    # def generate_routes(self, dfs: list[list[str]]):
    #     routes = []

        print(
            "===================================================================")
