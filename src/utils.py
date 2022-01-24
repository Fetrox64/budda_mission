def logger(message):
    print(f'''[BUDDA] {message}''')


def line():
    print("===================================================================")


BFS_TEST_MODEL_NORMAL = [
    ['A', 0],
    ['B', 1],
    ['D', 1],
    ['C', 2],
    ['E', 2],
    ['G', 2],
    ['F', 3],
    ['H', 3],
    ['J', 3],
    ['I', 4],
    ['K', 4]
]

BFS_TEST_MODEL_RED = [
    ['A', 0],
    ['B', 1],
    ['D', 0],
    ['C', 2],
    ['E', 2],
    ['G', 1],
    ['F', 3],
    ['H', 3],
    ['J', 2],
    ['I', 4],
    ['K', 4]
]

BFS_TEST_MODEL_GREEN = [
    ['A', 0],
    ['B', 1],
    ['D', 1],
    ['C', 2],
    ['E', 2],
    ['G', 2],
    ['F', 0],
    ['H', 3],
    ['J', 3],
    ['I', 0],
    ['K', 4]
]

NORMAL_TEST_ROUTES = [
    ['A', 'D', 'G', 'J', 'K'],
    ['A', 'B', 'E', 'H', 'K']
]

RED_TEST_ROUTE = ['A', 'G', 'J', 'K']

GREEN_TEST_ROUTE = ['A', 'B', 'C', 'K']
