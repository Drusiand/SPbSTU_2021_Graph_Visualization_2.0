from typing import List, Any, Union


class Stack:
    __data: List = list()

    """

    Stack implementation

    Attributes
    ----------
    __data: list
            Stack data

    Methods
    ----------
    add(self, added_element: str) -> None
            Adding new element in stack

    get(self) -> any
            Getting stack element

    is_empty(self) -> bool
            Check if stack is empty

    """

    def add(self, added_element: str) -> None:
        """

        Adding new element in stack

        Parameters
        ----------
        added_element:  str
                        new stack element

        """
        self.__data.append(added_element)

    def get(self) -> Any:
        """

        Getting stack element

        Returns
        ----------
        Available stack element

        """
        return self.__data.pop()

    def is_empty(self) -> bool:
        """

        Check if stack is empty

        Returns
        ----------
        True, if stack is empty; False otherwise

        """
        return len(self.__data) == 0


class Queue:
    __data: List = list()

    """

    Queue implementation

    Attributes
    ----------
    __data: list
            Queue data

    Methods
    ----------
    add(self, added_element: str) -> None
            Adding new element in queue

    get(self) -> any
            Getting queue element

    is_empty(self) -> bool
            Check if queue is empty

    """

    def add(self, added_element: str):
        """

        Adding new element in queue

        Parameters
        ----------
        added_element:  str
                        new queue element

        """
        self.__data.append(added_element)

    def get(self):
        """

        Getting queue element

        Returns
        ----------
        Available queue element

        """
        return self.__data.pop(0)

    def is_empty(self):
        """

        Check if queue is empty

        Returns
        ----------
        True, if queue is empty; False otherwise

        """
        return len(self.__data) == 0


def graph_traversal(graph, start: str, container_class: Union[Stack, Queue]) -> list:
    """

    General traversal function

    Parameters
    ----------
    graph:  Graph
            Graph instance

    start:  str
            Graph traversal start node

    container_class: Queue or Stack
            temporary container for graph traversal

    Returns
    ----------
    Traversal order (depends on chosen container)

    """
    visited_nodes = set()
    order = list()
    container = container_class
    container.add(start)
    while not container.is_empty():
        visited_node = container.get()
        order.append(visited_node)
        visited_nodes.add(visited_node)
        for unvisited_node in graph[visited_node]:
            if unvisited_node in visited_nodes:
                continue
            container.add(unvisited_node)
    return order


def dfs(graph, start: str) -> list:
    """

    DFS traversal function

    Parameters
    ----------
    graph:  Graph
            Graph instance

    start:  str
            Graph traversal start node

    Returns
    ----------
    DFS traversal order (depends on chosen container)

    """
    return graph_traversal(graph, start, Stack())


def bfs(graph, start: str) -> list:
    """

    BFS traversal function

    Parameters
    ----------
    graph:  Graph
            Graph instance

    start:  str
            Graph traversal start node

    Returns
    ----------
    BFS traversal order (depends on chosen container)

    """
    return graph_traversal(graph, start, Queue())
