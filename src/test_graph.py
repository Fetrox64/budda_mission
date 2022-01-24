import unittest
from main import generate_graph
from src.metro_graph import VERTEX_SET, EDGES_SET
from src.utils import BFS_TEST_MODEL_NORMAL, BFS_TEST_MODEL_RED, BFS_TEST_MODEL_GREEN
from src.utils import NORMAL_TEST_ROUTES, RED_TEST_ROUTE, GREEN_TEST_ROUTE


class GhaphTest(unittest.TestCase):

    def setUp(self):
        self.graph = generate_graph(VERTEX_SET, EDGES_SET)
        self.initial_node = self.graph.vertex_set['A']
        self.end_node = self.graph.vertex_set['K']
        self.route = 'RED'  # Change me

    def test_bfs(self):
        res = self.graph.bfs(self.initial_node, self.route)
        if self.route == 'NORMAL':
            self.assertEqual(res, BFS_TEST_MODEL_NORMAL)
        if self.route == 'RED':
            self.assertEqual(res, BFS_TEST_MODEL_RED)
        if self.route == 'GREEN':
            self.assertEqual(res, BFS_TEST_MODEL_GREEN)

    def test_generate_routes(self):
        self.graph.bfs(self.initial_node, self.route)
        initial_node = self.initial_node
        end_node = self.end_node
        route = self.route
        res = self.graph.generate_routes(initial_node, end_node, route)
        if self.route == 'NORMAL':
            self.assertIn(res, NORMAL_TEST_ROUTES)
        if self.route == 'GREEN':
            self.assertEqual(res, GREEN_TEST_ROUTE)
        if self.route == 'RED':
            self.assertEqual(res, RED_TEST_ROUTE)


if __name__ == "__main__.py":
    unittest.main()
