from collections import defaultdict


class Node:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self._name


class Edge:

    def __init__(self, src, dst):
        self._src = src
        self._dst = dst

    @property
    def source(self):
        return self._src

    @property
    def destination(self):
        return self._dst

    def __str__(self):
        return "%s -> %s" % (self.source, self.destination)


class WeightEdge(Edge):

    def __init__(self, src, dst, weight):
        super().__init__(src, dst)
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    def __str__(self):
        return "%s -> %s  [weight:%r]" % (self.source, self.destination, self.weight)


class Digraph:

    def __init__(self):
        self._nodes = list()
        self._edges = defaultdict(lambda: list())

    def add_node(self, node):
        if node in self._nodes:
            print("%s already in list" % node)
            return Node
        self._nodes.append(node)

    def add_edge(self, edge):
        if edge.source not in self._nodes and edge.destination not in self._nodes:
            print("edge %s is invalid" % edge)
        print("+ %s -> %s" % (edge.source, edge.destination))
        self._edges[edge.source].append(edge.destination)

    def children_of(self, node):
        return self._edges[node]

    def has_node(self, node):
        return node in self._nodes

    def __str__(self):
        res = ""
        for s in self._nodes:
            for d in self._edges[s]:
                res += "%s -> %s\n" % (s, d)
        return res

    def __iter__(self):
        yield from self._nodes


class Graph(Digraph):

    def add_edge(self, edge):
        super().add_edge(edge)
        super().add_edge(Edge(edge.destination, edge.source))
