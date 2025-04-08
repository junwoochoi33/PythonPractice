from src.misc.bfs import bfs
from src.misc.dfs import dfs
from src.misc.fibonacci_3 import fibonacci_3


def start():
    print("Application started!")

    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("BFS: ")
    bfs(graph, 'A')
    print("\nDFS: ")
    dfs(graph, 'A')

