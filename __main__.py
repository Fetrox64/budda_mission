import metro_graph as ghaph_description
from graph import Graph
from vertex import Vertex


def logger(message):
    print(f'''[BUDDA] {message}''')


def generate_graph(VERTEX_SET, EDGES_SET):
    print("========================================================")

    logger('Starting...')
    logger('Creating graph...')
    my_graph = Graph()
    logger('Adding vertexs...')
    for v in VERTEX_SET:
        my_graph.addVertex(v)
    logger('Adding edges...')
    for e in EDGES_SET:
        my_graph.addEdge(e)
    logger('Graph created')

    print("========================================================")

    return my_graph


def ask_for_initial_node(my_graph: Graph):
    logger('Asking for initial node...')
    aux = 'A'
    initial_node: Graph = my_graph.vertex_set[aux]
    return initial_node


def ask_for_end_node(my_graph: Graph):
    logger('Asking for end node...')
    aux = 'K'
    end_node: Graph = my_graph.vertex_set[aux]
    return end_node


def ask_for_route():
    logger('Asking for route...')
    route = 'NORMAL'
    return route


def bfs(my_graph, initial_node, end_node, route):
    print("========================================================")
    logger('Starting search...')
    logger(f'''Graph: {my_graph}''')
    logger(f'''Initial Node: {initial_node}''')
    logger(f'''End Node: {end_node}''')
    logger(f'''Route: {route}''')


def main():
    VERTEX_SET = ghaph_description.VERTEX_SET
    EDGES_SET = ghaph_description.EDGES_SET
    my_graph = generate_graph(VERTEX_SET, EDGES_SET)
    logger('Welcome!')
    initial_node = ask_for_initial_node(my_graph)
    end_node = ask_for_end_node(my_graph)
    route = ask_for_route()
    bfs(my_graph, initial_node, end_node, route)


if __name__ == '__main__':
    main()
