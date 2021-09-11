from collections import defaultdict
from python.graph_parser import GraphParser
import networkx as nx  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from python.gif_builder import GifBuilder  # type: ignore


class Graph:
    """
        Graph implementation

        Attributes
        ----------
        __graph_data:   defaultdict
                        Dictionary with nodes as keys and list of adjacent nodes as value

        Methods
        ----------
        draw(self, show_plot: bool = True, frame: list = None) -> None
                        Draw graph;

        build_gif(self, options: dict) -> bool
                        Build gif of the graph traversal;

        nodes()
                        getter for graph nodes

        edges()
                        getter for graph edges

        get_graph_dict()
                        getter for graph as dictionary

        get_start()
                        getter for start traversal node

        build_graph_from_file(filename: str)
                        initializer for graph from txt-file
        """

    def __init__(self, edges: defaultdict) -> None:
        self.__graph_data = edges

    def __getitem__(self, key: str) -> defaultdict:
        return self.__graph_data[key]

    def __len__(self) -> int:
        return len(self.__graph_data)

    def draw(self, show_plot: bool = True, node_colors: list = None) -> None:
        """

        Draw graph;

        Parameters
        ----------
        show_plot:      optional, bool, default = True
                        defines whether to show or not graph as networkx plot;

        node_colors:    array-like, optional, default = None
                        defines a colormap for each graph node;
        """
        draw_options = {
            "alpha": 0.8,
            "width": 3,
            "node_size": 700,
            "font_size": "15",
            "font_weight": "bold"
        }
        graph_layout = nx.planar_layout
        drawable_graph = nx.from_dict_of_lists(self.__graph_data)
        nx.draw(drawable_graph, with_labels=True, pos=graph_layout(drawable_graph), node_color=node_colors,
                **draw_options)
        if show_plot:
            plt.show()

    def build_gif(self, options: dict) -> bool:
        """

        Build gif of the graph traversals;

        Parameters
        ----------
        options:    dict
                    dictionary with desired gif name as key and desired traversal order as value

        Returns
        ----------
        True, if gifs build successfully, False otherwise

        """
        return GifBuilder.build(self, options)

    def nodes(self) -> list:
        """

        getter for graph nodes

        Returns
        ---------
        list of graph nodes

        """
        return list(self.__graph_data.keys())

    def edges(self) -> list:
        """

        getter for graph edges

        Returns
        ---------
        list of graph edges

        """
        return list(self.__graph_data.values())

    def get_graph_dict(self) -> defaultdict:
        """

        getter for graph as dictionary

        Returns
        ---------
        Graph as dictionary

        """
        return self.__graph_data

    def get_start(self) -> str:
        """

        getter for start traversal node

        Returns
        ---------
        start traversal node as string

        """
        return list(self.__graph_data.keys())[0]

    @staticmethod
    def build_graph_from_file(filename: str):  # -> Graph?
        """

        initializer for graph from txt-file

        Parameters
        ----------
        filename:   str
                    txt-source of graph

        Returns
        ----------
        Graph instance

        """
        edges = GraphParser.parse_graph(filename)
        return Graph(edges)
