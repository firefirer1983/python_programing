from node import Node, Graph, Edge, Digraph


class Path:

    def __init__(self, iterable):
        self._data = list(iterable)

    def __repr__(self):
        res = ""
        for i, d in enumerate(self._data):
            res += str(d)
            if i < len(self._data) - 1:
                res += ' -> '
        return res

    def append(self, data):
        self._data.append(data)

    def __iter__(self):
        yield from self._data

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]


def print_path(path):
    """
    path 是节点列表
    """
    result = ''
    for i, p in enumerate(path):
        result += str(p)
        if i < len(path) - 1:
            result += ' -> '
    return result


def depth_first(graph, start, end, path, shortest):
    print("DFS %s -> %s path:%r" % (start, end, path))
    # path 必须每个迭代使用新的来记录
    path = Path(path)
    path.append(start)
    if start == end:
        return path

    for node in graph.children_of(start):
        if node in path:
            continue
        if shortest is None or len(path) < len(shortest):
            new_path = depth_first(graph, node, end, path, shortest)
            if new_path:
                shortest = new_path
    return shortest


def broad_first(graph, start, end):
    init_path = Path([start])
    paths_checked = [init_path]
    while len(paths_checked):
        print("BFS: checked:%r" % paths_checked)
        path = paths_checked.pop()
        print("BFS: path:%r" % path)
        for n in graph.children_of(path[-1]):
            if n in path:
                continue
            new_path = Path(path)
            new_path.append(n)
            if n == end:
                return new_path
            paths_checked.append(new_path)


def make_test_graph():
    nodes = []
    for n in range(6):
        nodes.append(Node(str(n)))
    g = Digraph()
    for n in nodes:
        print("+ %s" % n)
        g.add_node(n)
    print("Graph nodes number: ", len(g._nodes))

    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[0]))
    g.add_edge(Edge(nodes[3], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[0]))
    print("Graph:")
    print(g)
    for n in g:
        print("%s children:" % n)
        print("%r" % [str(c) for c in g.children_of(n)])
    shortest = depth_first(g, nodes[0], nodes[5], list(), None)
    print("DFS Shortest path: %r" % shortest)

    shortest = broad_first(g, nodes[0], nodes[5])
    print("BFS Shortest path: %r" % shortest)


if __name__ == '__main__':
    make_test_graph()
