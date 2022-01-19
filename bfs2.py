from graph import Graph
from vertex import Vertex
from logger import logger


def bfs2(my_graph: Graph, initial_node: Vertex, end_node: Vertex, route: str):
    print("===================================================================")
    logger('Starting search...')
    logger(f'''Graph: {my_graph}''')
    logger(f'''Initial Node: {initial_node}''')
    logger(f'''End Node: {end_node}''')
    logger(f'''Route: {route}''')
    print("===================================================================")

    start_id = initial_node.id
    end_id = end_node.id
    vertex_list = []

    for v in my_graph.vertex_set:
        vertex_list.append(v)

    if start_id in vertex_list and end_id in vertex_list:
        # Set the queue
        routes = []
        routes.append(initial_node)

        # Save the explored nodes
        explored = []
        explored.append(initial_node)
        new_route, actual_route, actual_node_id, actual_node, actual_neighbor_id, actual_neighbor, output = ''

        while len(route) > 0:
            del routes[0]
            actual_route = routes


#       //Mientras hayan rutas por explorar
#       while (rutas.length > 0) {
#           ruta_actual = rutas.shift();
#           nodo_actualID = ruta_actual[ruta_actual.length-1];
#           nodo_actual = this.vertices[this.getVertexIndex(nodo_actualID)];

#           //Analizamos cada uno de los vecinos del nodo actual en la ruta
#           for (let i = 0; i < nodo_actual.neighbors.length; i++) {
#               vecino_actualID = nodo_actual.neighbors[i];
#               vecino_actual = this.vertices[this.getVertexIndex(vecino_actualID)];

#               if (explorados.includes(vecino_actualID)) {
#               } else {
#                   //Preguntamos si el nodo actual es el nodo destino
#                   if (vecino_actualID == finalVertex) {
#                       salida += `<h3>La ruta más corta de ` + this.vertices[startId].name + ` a ` + this.vertices[finalId].name + `</h3><div class='ruta'>`;

#                       for (let j = 0; j < ruta_actual.length; j++) {
#                           salida += `<span class='vertice'>` + this.vertices[this.getVertexIndex(ruta_actual[j])].name + `</span>`;
#                       }

#                       salida += `<span class='vertice'>` + this.vertices[this.getVertexIndex(vecino_actualID)].name + `</span></div>`;

#                       $("#sectionMapa").append("<img src='img/Loading.gif'>");

#                       setTimeout(() => {
#                           $("#sectionMapa").html("");
#                           $("#sectionMapa").append(salida);
#                       }, 1500);
#                   } else {
#                       nueva_ruta = ruta_actual.slice();
#                       nueva_ruta.push(vecino_actualID);
#                       rutas.push(nueva_ruta);
#                   }

#                   explorados.push(vecino_actualID);
#               }
#           }
#       }
