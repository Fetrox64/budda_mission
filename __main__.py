import metro_graph
from graph import Graph

VERTEX_SET = metro_graph.VERTEX_SET
EDGES_SET = metro_graph.EDGES_SET


def logger(message):
    print(f'''[BUDDA] {message}''')


def main():
    print("========================================================")

    logger('Starting...')
    logger('Creating graph...')
    graph = Graph()
    logger('Adding vertexs...')
    for v in VERTEX_SET:
        graph.addVertex(v)
    logger('Adding edges...')
    for e in EDGES_SET:
        graph.addEdge(e)
    logger('Edges added')
    logger('Graph created')

    print("========================================================")


if __name__ == '__main__':
    main()
