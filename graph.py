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

    def bfs(self, r):
        print("===================================================================")
        logger('Starting search...')
        # logger(f'''{self.vertex_set}''')
        if r in self.vertex_set:
            queue = [r]
            self.vertex_set[r].visited = True
            self.vertex_set[r].level = 0

            logger(f'''( {r}, {self.vertex_set[r].level} )''')

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
                        logger(f'''( {id}, {level} )''')
            print(
                "===================================================================")
