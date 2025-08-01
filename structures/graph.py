from typing import Dict, List, Tuple, Iterator, Hashable, Union


class Graph:
    """
    Universal graph supporting directed/undirected and weighted/unweighted modes.
    Internal representation: adjacency dictionary.

    Attributes:
        directed (bool): whether the graph is directed
        weighted (bool): whether edges have weights
        adj: Dict[node, Dict[node, weight]] — adjacency mapping
    """

    def __init__(
            self,
            directed: bool = False,
            weighted: bool = False
    ) -> None:
        self.directed = directed
        self.weighted = weighted
        self.adj: Dict[Hashable, Dict[Hashable, float]] = {}

    def add_node(self, u: Hashable) -> None:
        """Add a node u if it does not already exist."""
        self.adj.setdefault(u, {})

    def add_edge(
            self,
            u: Hashable,
            v: Hashable,
            weight: float = 1.0
    ) -> None:
        """
        Add edge u -> v (and v -> u if graph is undirected).
        Automatically creates nodes if they are missing.
        """
        self.add_node(u)
        self.add_node(v)
        self.adj[u][v] = weight
        if not self.directed:
            self.adj[v][u] = weight

    def remove_node(self, u: Hashable) -> None:
        """Remove node u and all edges incident to it."""
        if u not in self.adj:
            return
        del self.adj[u]
        for nbrs in self.adj.values():
            nbrs.pop(u, None)

    def remove_edge(self, u: Hashable, v: Hashable) -> None:
        """Remove edge u -> v (and v -> u if graph is undirected)."""
        self.adj.get(u, {}).pop(v, None)
        if not self.directed:
            self.adj.get(v, {}).pop(u, None)

    def neighbors(self, u: Hashable) -> List[Hashable]:
        """Return list of neighbors for node u."""
        return list(self.adj.get(u, {}))

    def has_edge(self, u: Hashable, v: Hashable) -> bool:
        """Check if edge u -> v exists."""
        return v in self.adj.get(u, {})

    def nodes(self) -> List[Hashable]:
        """Return list of all nodes in the graph."""
        return list(self.adj.keys())

    def edges(self) -> Iterator[Union[Tuple[Hashable, Hashable], Tuple[Hashable, Hashable, float]]]:
        """
        Iterator over edges:
        - unweighted: yields (u, v)
        - weighted: yields (u, v, weight)
        For undirected graphs, each edge is yielded only once.
        """
        seen = set()
        for u, nbrs in self.adj.items():
            for v, w in nbrs.items():
                if self.directed:
                    yield (u, v, w) if self.weighted else (u, v)
                else:
                    if (v, u) in seen:
                        continue
                    seen.add((u, v))
                    yield (u, v, w) if self.weighted else (u, v)

    def degree(self, u: Hashable) -> Union[int, Tuple[int, int]]:
        """
        Return degree of node u:
        - undirected: returns int
        - directed: returns (in_degree, out_degree)
        """
        out_deg = len(self.adj.get(u, {}))
        if not self.directed:
            return out_deg
        in_deg = sum(1 for nbrs in self.adj.values() if u in nbrs)
        return in_deg, out_deg

    def __len__(self) -> int:
        """Return number of nodes in the graph."""
        return len(self.adj)

    def __contains__(self, u: object) -> bool:
        """Check if node u exists in the graph."""
        return u in self.adj

    def __iter__(self) -> Iterator[Hashable]:
        """Iterate over nodes in the graph."""
        return iter(self.adj)

    def __str__(self) -> str:
        """Return string representation of the graph for debugging."""
        lines = []
        for u, nbrs in self.adj.items():
            if self.weighted:
                for v, w in nbrs.items():
                    lines.append(f"{u} -> {v} [weight={w}]")
            else:
                for v in nbrs.keys():
                    lines.append(f"{u} -> {v}")
        return "\n".join(lines)

    def clear(self) -> None:
        """Remove all nodes and edges from the graph."""
        self.adj.clear()
