import re

graph = {}

with open("inputs/aoc_input_7.txt") as f:
    for line in f:
        colors = re.split(" bags contain \d | bags?, \d | bags?.", line.rstrip())[:-1]
        numbers = [int(s) for s in line.split() if s.isdigit()]
        if colors[1] == "contain no other":
            graph[colors[0]] = list()
        else:
            graph[colors[0]] = list(zip(colors[1:], numbers))


# PART 1
def how_many_can_contain(color, graph):
    n = 0
    for node in graph:
        if is_reachable(node, color, graph):
            n += 1
    return n - 1    # assuming a bag does not have to contain a bag of the same color (ininite recursion!)

def is_reachable(s, t, graph):
    """Returns if there is a path from node s to node t in the graph with a simple BFS approach

    Args:
        s (node): start node
        t (node): end node
        graph (dict of node -> list of edges): representation of graph
    """
    visited = [s,]
    queue = [s,]

    while queue:
        cur = queue.pop(0)
        if cur == t:
            return True
        else:
            for neighbour in graph[cur]:
                if neighbour not in visited:
                    queue.append(neighbour[0])
                    visited.append(neighbour[0])
    
    return False


# PART 2
def contains_how_many(color, graph):
    if graph[color] == []:
        return 1
    else:
        return __contains_how_many__(set(), dict(), color, graph)

def __contains_how_many__(visited, contains, node, graph):
    """Calculates the number of bags in the given bag with a recursive DFS approach

    Args:
        visited (list of nodes): nodes that have been already visited
        contains (dict of node -> int): how many bags are in a single bag (to avoid recalculations)
        node (node): the node to calculate the number of contained bags of
        graph (dict of node -> list of edges): representation of graph
    """
    if node not in visited:
        visited.add(node)
        if graph[node] == []:
            contains[node] = 0
            return 0
        else:
            n = 0
            for neighbour in graph[node]:
                n += neighbour[1] * __contains_how_many__(visited, contains, neighbour[0], graph) + neighbour[1]
            contains[node] = n
            return n
    else:
        return contains[node]


print("Part 1: " + str(how_many_can_contain("shiny gold", graph)))
print("Part 2: " + str(contains_how_many("shiny gold", graph)))