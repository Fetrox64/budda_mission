import metro_graph


class Vertex:
    def __init__(self, letter, name, route):
        self.id = letter
        self.name = name
        self.route = route
        self.neighbors = []


class Graph:
    def __init__(self):
        self.vertex = []


def logger(message):
    print(f'''[BUDDA] {message}''')


def main():
    print("==============================")
    logger('Iniciando programa...')
    print("==============================")


if __name__ == '__main__':
    main()
