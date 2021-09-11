import pytest  # type: ignore
from python.graph import Graph
import networkx as nx  # type: ignore
from python.graph_algorithms import dfs, bfs


def test_graph_build():
    """
    Test function to check if graphs vere initialized as expected
    """
    graph_letters = Graph.build_graph_from_file("data/graph_example/graph_letters.txt")
    graph_numbers = Graph.build_graph_from_file("data/graph_example/graph_numbers.txt")
    wrong_graph_count = 0
    try:
        Graph.build_graph_from_file("data/graph_example/graph_incorrect.txt")
    except ValueError:
        wrong_graph_count += 1
    graph_empty = Graph.build_graph_from_file("data/graph_example/graph_empty.txt")
    if len(graph_empty.get_graph_dict()) == 0:
        wrong_graph_count += 1
    assert wrong_graph_count == 2
    return [graph_numbers, graph_letters]


valid_graphs = test_graph_build()


def test_BFS():
    """
    Test function for comparison of custom and networkx built-in functions of BFS
    """
    for valid_graph in valid_graphs:
        nx_graph = nx.from_dict_of_lists(valid_graph.get_graph_dict())
        nx_bfs = [nodes for nodes in nx.bfs_tree(nx_graph, valid_graph.get_start())]
        assert bfs(valid_graph, valid_graph.get_start()) == nx_bfs


def test_DFS():
    """
    Test function for comparison of custom and networkx built-in functions of DFS
    """
    for valid_graph in valid_graphs:
        nx_graph = nx.from_dict_of_lists(valid_graph.get_graph_dict())
        nx_dfs = [nodes for nodes in nx.dfs_postorder_nodes(nx_graph, valid_graph.get_start())]
        nx_dfs.reverse()
        assert dfs(valid_graph, valid_graph.get_start()) == nx_dfs


def test_gif_builder():
    for valid_graph in valid_graphs:
        opts = {"./data/gif_test/bfs.gif": bfs(valid_graph, valid_graph.get_start()),
                "./data/gif_test/dfs.gif": dfs(valid_graph, valid_graph.get_start())}
        valid_graph.build_gif(opts)
