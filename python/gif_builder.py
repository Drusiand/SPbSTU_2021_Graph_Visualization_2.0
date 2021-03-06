import matplotlib.pyplot as plt  # type: ignore
from celluloid import Camera  # type: ignore


def get_frames(graph, traversal_order: list, unvisited_node_color: str = "red",
               visited_node_color: str = "blue") -> list:
    """

    Get color frames of based on graph traversal order

    :param graph:  Graph
            Graph instance

    :param traversal_order:    list
                        input graph traversal order

    :param unvisited_node_color:   str
                            color of unvisited graph node

    :param visited_node_color:     str
                            color of visited graph node

    :return: list:
            list of traversal frames

    """
    frames = list()
    initial_frame = list()
    for i in range(len(graph)):
        initial_frame.append(unvisited_node_color)
    frames.append(initial_frame)
    for node in traversal_order:
        tmp_frame = frames[-1].copy()
        tmp_frame[graph.nodes().index(node)] = visited_node_color
        frames.append(tmp_frame)
    return frames


class GifBuilder:
    """

    Gif builder implementation

    :Methods:
    ---------
    build(graph, gif_options: dict) -> bool
                gif builder

    """

    @staticmethod
    def build(graph, gif_options: dict) -> bool:
        """

        gif builder

        :param graph:  Graph
                Graph instance

        :param gif_options:    dict
                        dictionary with desired gif name as key and desired traversal order as value

        :return: bool:
                True, if gifs build successfully; False otherwise

        """
        for gif_name in gif_options:
            frames = get_frames(graph, gif_options[gif_name])
            fig = plt.figure()
            camera = Camera(fig)
            for frame in frames:
                graph.draw(show_plot=False, node_colors=frame)
                camera.snap()
            animation = camera.animate(interval=1000)
            animation.save(gif_name)
        return True
