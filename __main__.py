from metro_graph import VERTEX_SET, EDGES_SET
from utils import logger, line
from graph import Graph
from vertex import Vertex


def generate_graph(VERTEX_SET, EDGES_SET):
    line()
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
    line()
    return my_graph


def ask_for_initial_node(my_graph: Graph):
    id_list = list(my_graph.vertex_set.keys())
    first_node = id_list[0]
    last_node = id_list.pop()
    id_list = list(my_graph.vertex_set.keys())
    input_id = input(
        f'''[BUDDA] Input an initial station id between {first_node} and {last_node} : ''').upper()
    while input_id not in id_list:
        logger('Introduce a correct key')
        input_id = input(
            f'''[BUDDA] Input an initial station id between {first_node} and {last_node} : ''').upper()
    initial_node: Vertex = my_graph.vertex_set[input_id]
    return initial_node


def ask_for_end_node(my_graph: Graph, initial_node: Vertex):
    id_list = list(my_graph.vertex_set.keys())
    first_node = id_list[0]
    last_node = id_list.pop()
    id_list = list(my_graph.vertex_set.keys())
    input_id = input(
        f'''[BUDDA] Input an destination station id between {first_node} and {last_node} : ''').upper()
    while input_id == initial_node.id:
        logger('Same station are not allowed')
        input_id = input(
            f'''[BUDDA] Input an destination station id between {first_node} and {last_node} : ''').upper()
    while input_id not in id_list:
        logger('Introduce a correct key')
        input_id = input(
            f'''[BUDDA] Input an destination station id between {first_node} and {last_node} : ''').upper()
    end_node: Vertex = my_graph.vertex_set[input_id]
    return end_node


def ask_for_route():
    return 'NORMAL'
    avaliable_routes = ['NORMAL', 'RED', 'GREEN']
    route = input('[BUDDA] Input a route: ').upper()

    while route not in avaliable_routes:
        logger('Introduce a correct route')
        logger(f'''Avaliable routes: {' - '.join(avaliable_routes)}''')
        route = input('[BUDDA] Input a route: ').upper()
    return route


def main():
    my_graph = generate_graph(VERTEX_SET, EDGES_SET)
    logger('Welcome!')
    initial_node = ask_for_initial_node(my_graph)
    end_node = ask_for_end_node(my_graph, initial_node)
    route = ask_for_route()
    bfs_data = my_graph.bfs(initial_node, end_node, route)
    logger(bfs_data)
    # my_graph.generate_routes(bfs_data)
    line()


if __name__ == '__main__':
    main()
