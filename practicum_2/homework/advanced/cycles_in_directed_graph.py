import networkx as nx


TEST_GRAPH_FILES = [
    "graph_1_wo_cycles.edgelist",
    "graph_2_wo_cycles.edgelist",
    "graph_3_w_cycles.edgelist",
]


def has_cycles(g: nx.DiGraph):
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        for neighbor in g.neighbors(node):
            if dfs(neighbor):
                return True

        stack.remove(node)
        return False

    for node in g.nodes:
        if dfs(node):
            return True
    return False


if __name__ == "__main__":
    for filename in TEST_GRAPH_FILES:
        G = nx.read_edgelist(f"practicum_2/homework/advanced/{filename}", create_using=nx.DiGraph)
        print(f"Graph {filename} has cycles: {has_cycles(G)}")
