from collections import defaultdict


class GraphParser:
    """

    Graph parser implementation

    Methods
    ----------
    parse_graph(source: str, node_edges_delimiter=":", token_delimiter=",") -> defaultdict
                parsing graph from txt-file

    """

    @staticmethod
    def parse_graph(source: str, node_edges_delimiter: str = ":", token_delimiter: str = ",") -> defaultdict:
        """

        Parsing graph from txt-file

        Parameters
        ----------
        source: str
                name of desired txt-file

        token_delimiter:
                delimiter between current node and adjacent ones

        node_edges_delimiter:
                delimiter among nodes adjacent to the certain one

        Returns
        ----------
        parsed_graph:   defaultdict
                        graph represented by dictionary {node: edges}

        """
        parsed_graph = defaultdict(list)
        with open(source, "r") as raw_graph:
            for line in raw_graph.readlines():
                node, neighbours = line.split(node_edges_delimiter)
                for neighbour in neighbours.strip().split(token_delimiter):
                    parsed_graph[node.strip()].append(neighbour)
        return parsed_graph
