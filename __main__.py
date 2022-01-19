import metro_graph as ghaph_description
from graph import Graph
from logger import logger
from vertex import Vertex


def generate_graph(VERTEX_SET, EDGES_SET):
    print("===================================================================")

    logger('Starting...')
    logger('Creating graph...')
    my_graph = Graph()
    logger('Adding vertexs...')
    for v in VERTEX_SET:
        my_graph.add_vertex(v)
    logger('Adding edges...')
    for e in EDGES_SET:
        my_graph.add_edge(e)
    logger('Graph created')

    print("===================================================================")

    return my_graph


def ask_for_initial_node(my_graph: Graph):
    logger('Asking for initial node...')
    aux = 'E'
    initial_node: Vertex = my_graph.vertex_set[aux]
    return initial_node


def ask_for_end_node(my_graph: Graph):
    logger('Asking for end node...')
    aux = 'D'
    end_node: Vertex = my_graph.vertex_set[aux]
    return end_node


def ask_for_route():
    logger('Asking for route...')
    route = 'NORMAL'
    return route


def main():
    VERTEX_SET = ghaph_description.VERTEX_SET
    EDGES_SET = ghaph_description.EDGES_SET
    my_graph = generate_graph(VERTEX_SET, EDGES_SET)
    logger('Welcome!')
    initial_node = ask_for_initial_node(my_graph)
    end_node = ask_for_end_node(my_graph)
    route = ask_for_route()
    my_graph.bfs(initial_node.id)


if __name__ == '__main__':
    main()
