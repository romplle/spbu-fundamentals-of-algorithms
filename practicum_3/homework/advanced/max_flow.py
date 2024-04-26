from typing import Any

import networkx as nx

def bfs(G, s, t, parent):
    visited = [False] * len(G.nodes())
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for v in G.neighbors(u):
            if not visited[v] and G[u][v]['weight'] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True

    return False

def max_flow(G: nx.Graph, s: Any, t: Any) -> int:
    parent = [-1] * len(G.nodes())
    max_flow: int = 0

    while bfs(G, s, t, parent):
        path_flow = float("inf")
        n = t
        while n != s:
            path_flow = min(path_flow, G[parent[n]][n]['weight'])
            n = parent[n]

        v = t
        while v != s:
            u = parent[v]
            G[u][v]['weight'] -= path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow


if __name__ == "__main__":
    # Load the graph
    G = nx.read_edgelist("practicum_3/homework/advanced/graph_1.edgelist", create_using=nx.DiGraph, nodetype=int)
    
    val = max_flow(G, s=0, t=5)
    print(f"Maximum flow is {val}. Should be 23")
