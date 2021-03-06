from search import *
import math
import heapq


def convert_to_list(map_string):
    """

    :param map_string: the string representation of the map.
    :return: the coordinate representations of obstacles, goals, agents, fueling points and the overall map dimensions.
    """
    agents = []
    goals = []
    obstacles = []
    fueling_points = []
    lines = map_string.split("\n")
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        if "|" in lines[i]:
            for j in range(1, len(lines[i]) - 1):
                if lines[i][j] == "X":
                    obstacles.append((i, j))
                elif lines[i][j] == "G":
                    goals.append((i, j))
                elif lines[i][j] == "F":
                    fueling_points.append((i, j))
                elif lines[i][j] != " ":
                    if lines[i][j] == "S":
                        agents.append((i, j, math.inf))
                    else:
                        agents.append((i, j, int(lines[i][j])))
    return obstacles, goals, agents, fueling_points, (len(lines) - 1, len(lines[0]))


def new_position(prev, move):
    """

    :param prev: the previous coordinates position
    :param move: the move to make from this position
    :return: the resulting new coordinates of adding the move to the previous coordinates.
    """
    return prev[0] + move[0], prev[1] + move[1]


class RoutingGraph(Graph):
    """
    This is the graph representation of the map string. A subclass of Graph from search.py.
    """
    def __init__(self, map_string):
        """
        This initialises the RoutingGraph instance.
        :param map_string: The string representation of the map.
        """
        self.obstacles, self.goals, self.start_nodes, self.fueling_points, self.size = convert_to_list(map_string)
        self.moves = {
            "S": (1, 0),
            "N": (-1, 0),
            "W": (0, -1),
            "E": (0, 1)
        }

    def is_goal(self, node):
        """
        Checks if a node is a goal.
        :param node: the node to check
        :return: True if the node is a goal, False otherwise.
        """
        return (node[0], node[1]) in self.goals

    def starting_nodes(self):
        """
        :return: The starting nodes of the graph.
        """
        return self.start_nodes

    def estimated_cost_to_goal(self, node):
        """
        This is the heuristic for the AStar search algorithm. It calculates the euclidean distance between the current
        node and the closest goal node.
        :param node: the node to calculate cost from.
        :return: the euclidean distance between node and the closest goal node.
        """
        distance = math.inf
        for goal in self.goals:
            euclid = abs(goal[0] - node.head[0]) + abs(goal[1] - node.head[1])
            if euclid < distance:
                distance = euclid
        return distance

    def outgoing_arcs(self, tail_node):
        """
        This calculates all the outgoing arcs from tail_node on the graph.
        :param tail_node: the node to calculate the outgoing arc from
        :return: all outgoing arcs in the graph from tail_node.
        """
        arcs = []
        if tail_node[2] > 0:
            if tail_node[0] > 1 and new_position(tail_node, self.moves["N"]) not in self.obstacles:
                arcs.append(Arc(tail_node, new_position(tail_node, self.moves["N"]) + tuple([tail_node[2] - 1]), "N", 5))

            if tail_node[1] < self.size[1] - 2 and new_position(tail_node, self.moves["E"]) not in self.obstacles:
                arcs.append(Arc(tail_node, new_position(tail_node, self.moves["E"]) + tuple([tail_node[2] - 1]), "E", 5))

            if tail_node[0] < self.size[0] - 2 and new_position(tail_node, self.moves["S"]) not in self.obstacles:
                arcs.append(Arc(tail_node, new_position(tail_node, self.moves["S"]) + tuple([tail_node[2] - 1]), "S", 5))

            if tail_node[1] > 1 and new_position(tail_node, self.moves["W"]) not in self.obstacles:
                arcs.append(Arc(tail_node, new_position(tail_node, self.moves["W"]) + tuple([tail_node[2] - 1]), "W", 5))

        if (tail_node[0], tail_node[1]) in self.fueling_points and tail_node[2] < 9:
            arcs.append(Arc(tail_node, (tail_node[0], tail_node[1], 9), "Fuel up", 15))
        return arcs


class AStarFrontier(Frontier):
    """
    This class is the frontier for the AStar graph search algorithm. A subclass of Frontier in the search.py module.
    """
    def __init__(self, map_graph):
        """
        Initialises the AStarFrontierInstance
        :param map_graph: RoutingGraph instance representing the map.
        """
        self.map = map_graph
        self.container = []
        self.expanded = set()
        self.counter = 0

    def add(self, path):
        """
        Adds the path to the heap if it has not already been expanded by the search algorithm.
        :param path: the path to the current node.
        :return: None
        """
        if path[-1].head not in self.expanded:
            path_cost = 0
            for i in range(0, len(path)):
                path_cost += 1
            path_cost += self.map.estimated_cost_to_goal(path[-1])
            entry = (path_cost, self.counter, path)
            self.counter += 1
            heapq.heappush(self.container, entry)

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next node to expand.
        :return: The next node to expand
        """
        if len(self.container) > 0:
            item = heapq.heappop(self.container)
            while item[2][-1].head in self.expanded:
                if len(self.container) > 0:
                    item = heapq.heappop(self.container)
                else:
                    raise StopIteration
            self.expanded.add(item[2][-1].head)
            return item[2]
        else:
            raise StopIteration


def get_heads(arcs):
    """
    Gets the head node from the arcs
    :param arcs: arcs to get the head nodes from
    :return: head, the heads from the given arcs.
    """
    heads = []
    if arcs is not None:
        for arc in arcs:
            heads.append(arc.head)
    return heads


def print_map(graph, frontier, solution):
    """
    Print out the solution to the map.
    :param graph: the RoutingGraph instance representing the map.
    :param frontier: the AStarFrontier instance that solved the map.
    :param solution: the solution to the map.
    :return: None
    """
    size = graph.size
    output = "+" + (size[1] - 2) * "-" + "+\n"
    line_count = 0
    solution_path = get_heads(solution)
    expanded = frontier.expanded
    for i in range(size[1] + 1, (size[0] - 1) * size[1] + 1):
        if i % size[1] == 1:
            output += "|"
        elif i % size[1] == 0:
            output += "|\n"
            line_count += 1
        else:
            if (line_count + 1, i % size[1] - 1) in graph.goals:
                output += "G"
            elif (line_count + 1, i % size[1] - 1, math.inf) in graph.start_nodes:
                output += "S"
            elif (line_count + 1, i % size[1] - 1, math.inf) in solution_path:
                output += "*"
            elif (line_count + 1, i % size[1] - 1, math.inf) in expanded:
                output += "."
            elif (line_count + 1, i % size[1] - 1) in graph.obstacles:
                output += "X"
            else:
                output += " "
    output += "+" + (size[1] - 2) * "-" + "+\n"
    print(output)



