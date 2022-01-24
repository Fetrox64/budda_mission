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

    def bfs(self, initial_node: Vertex, route: str):
        line()
        logger('Starting search...')
        i = initial_node.id

        if i in self.vertex_set:
            bfs_data = []
            queue = [i]
            self.vertex_set[i].visited = True
            self.vertex_set[i].level = 0
            bfs_data.append([i, self.vertex_set[i].level])

            while len(queue) > 0:
                current = queue[0]
                queue = queue[1:]

                for v in self.vertex_set[current].neighbor_set:
                    v = v.id

                    if self.vertex_set[v].visited == False:
                        queue.append(v)
                        self.vertex_set[v].visited = True
                        node_route = self.vertex_set[v].route

                        if node_route == 'RED' and route == 'GREEN':
                            self.vertex_set[v].level = 0
                        elif node_route == 'GREEN' and route == 'RED':
                            self.vertex_set[v].level = 0
                        else:
                            self.vertex_set[v].level = self.vertex_set[current].level + 1

                        bfs_data.append(
                            [self.vertex_set[v].id, self.vertex_set[v].level])

            return bfs_data

    def generate_routes(self, initial_node: Vertex, end_node: Vertex, route: str):
        path = []
        current = initial_node
        distance = end_node.level
        founded = False

        while not founded:

            if route != 'NORMAL':

                for n in range(distance + 1):
                    if current.route == 'RED' and route == 'RED':
                        path.append(current.id)
                        current = choice(
                            self.vertex_set[current.id].neighbor_set)
                    elif current.route == 'GREEN' and route == 'GREEN':
                        path.append(current.id)
                        current = choice(
                            self.vertex_set[current.id].neighbor_set)
                    elif current.route == 'NORMAL':
                        path.append(current.id)
                        current = choice(
                            self.vertex_set[current.id].neighbor_set)
                    while current.route == 'GREEN' and route == 'RED':
                        current = choice(current.neighbor_set)
                    while current.route == 'RED' and route == 'GREEN':
                        current = choice(current.neighbor_set)

            else:
                for n in range(distance + 1):
                    path.append(current.id)
                    current = choice(self.vertex_set[current.id].neighbor_set)

            last_node = path.copy().pop()

            if last_node == end_node.id:
                logger(f'''Best route: {' -> '.join(path)}''')
                founded = True
                break
            else:
                path = []
                current = initial_node

        return path
