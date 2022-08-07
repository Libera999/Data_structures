# define class for the graphs
# methods for finding all paths in a graph and the shortest path between nodes

from collections import deque


class Graph:
    def __init__(self, graph_value):
        self.gr = graph_value

    def find_all_paths(self, start, end, path=[]):  # Depth-First Search
        path = path + [start]
        if start == end:
            return [path]

        paths = []
        for node in self.gr[start]:
            # next node
            if node not in path:
                new_ps = self.find_all_paths(node, end, path)
                for new_p in new_ps:
                    paths.append(new_p)
        return paths

    # Breadth-First Search - start with arbitrary node and explore all neighbours of a node
    # time complexity N + edges
    def search(self, root, node):
        visited = []
        path = deque([root])
        visited.append(root)
        all_nodes = list(self.gr.keys())  # put all nodes in a list

        while all_nodes:

            while path:
                s = path.pop()

                if s == node:
                    return True

                all_nodes.remove(s)

                for neighbour in self.gr[s]:
                    if neighbour == node:
                        return True
                    if neighbour not in visited:
                        visited.append(neighbour)
                        path.append(neighbour)

                # if the node is not reachable from initial root, we continue
                if path == deque([]) and all_nodes:
                    path.append(all_nodes[0])

        return False


# graph as a dictionary
g = {'A': ['B', 'C'],
     'B': ['C', 'D'],
     'C': ['D'],
     'D': ['C'],
     'E': ['F'],
     'F': ['C']}

graph = Graph(g)

print("Graph: ", graph.gr)  # graph

print("All paths: ", graph.find_all_paths('A', 'D'))  # all paths

root = list(graph.gr.keys())[0]  # set an arbitraty root for search
node = 'E'
print(f"Is there an element {node}: ", graph.search(root, node))
