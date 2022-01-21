from gettext import find
from random import choice
from src.utils import logger, line
from src.vertex import Vertex


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
        line()
        logger('Starting search...')
        i = initial_node.id
        e = end_node.id

        if i in self.vertex_set and e in self.vertex_set:
            queue = [i]
            self.vertex_set[i].visited = True
            self.vertex_set[i].level = 0

            while len(queue) > 0:
                current = queue[0]
                queue = queue[1:]

                for v in self.vertex_set[current].neighbor_set:
                    v = v.id

                    if self.vertex_set[v].visited == False:
                        queue.append(v)
                        self.vertex_set[v].visited = True
                        self.vertex_set[v].level = self.vertex_set[current].level + 1

    def bfs_with_colors(self, initial_node: Vertex, end_node: Vertex, route: str):
        line()
        logger('Starting search with colors...')
        i = initial_node.id
        e = end_node.id

        if i in self.vertex_set and e in self.vertex_set:
            queue = [i]
            self.vertex_set[i].visited = True
            self.vertex_set[i].level = 0

            while len(queue) > 0:
                current = queue[0]
                queue = queue[1:]

                for v in self.vertex_set[current].neighbor_set:
                    v = v.id

                    if self.vertex_set[v].visited == False:
                        queue.append(v)
                        self.vertex_set[v].visited = True
                        self.vertex_set[v].level = self.vertex_set[current].level + 1

    def generate_routes(self, initial_node: Vertex, end_node: Vertex):
        route = []
        current = initial_node
        distance = end_node.level
        founded = False

        while not founded:

            for n in range(distance + 1):
                route.append(current.id)
                current = choice(self.vertex_set[current.id].neighbor_set)

            last_node = route.copy().pop()

            if last_node == end_node.id:
                logger(f'''Best route: {' - '.join(route)}''')
                founded = True
                break
            else:
                route = []
                current = self.vertex_set[initial_node.id]
