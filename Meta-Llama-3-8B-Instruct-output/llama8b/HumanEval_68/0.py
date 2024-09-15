def pluck(arr):
    even_nodes = [(node, i) for i, node in enumerate(arr) if node % 2 == 0]
    if not even_nodes:
        return []
    even_nodes.sort(key=lambda x: (x[0], x[1]))
    return [even_nodes[0][0], even_nodes[0][1]]