from search import *
from superquiz import *


def test1():
    print("\nStarting Test 1\n")
    map_str = """\
    +-------+
    |  9  XG|
    |X XXX  |
    | S  0FG|
    +-------+
    """

    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at starting states:")
    for s in sorted(graph.starting_nodes()):
        print(s)
        for arc in graph.outgoing_arcs(s):
            print("  " + str(arc))

    node = (1, 1, 5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    node = (1, 7, 2)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    node = (3, 7, 0)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3, 7, math.inf)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3, 6, 5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    node = (3, 6, 9)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))
    print("\nEnd of Test 1\n")


def test2():
    print("\nStarting Test 2\n")
    map_str = """\
    +--+
    |GS|
    +--+
    """

    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at the start:")
    for start in graph.starting_nodes():
        for arc in graph.outgoing_arcs(start):
            print("  " + str(arc))

    node = (1, 1, 1)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))
    print("\nEnd of Test 2\n")


def test3():
    print("\nStarting Test 3\n")
    map_str = """\
    +------+
    |S    S|
    |  GXXX|
    |S     |
    +------+
    """

    graph = RoutingGraph(map_str)
    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("\nEnd of Test 3\n")


def test4():
    map_str = """\
    +-------+
    |   G   |
    |       |
    |   S   |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def test5():
    map_str = """\
    +-------+
    |  GG   |
    |S    G |
    |  S    |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def test6():
    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def test8():
    map_str = """\
    +----------+
    |    X     |
    | S  X  G  |
    |    X     |
    +----------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def test7():
    map_str = """\
    +-------+
    |  F  X |
    |X XXXXG|
    | 3     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def test9():
    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def test10():
    map_str = """\
    +---+
    |GF2|
    +---+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def test11():
    map_str = """\
    +----+
    | S  |
    | SX |
    |GX G|
    +----+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def test12():
    map_str = """\
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def test13():
    map_str = """\
    +----------------+
    |2              F|
    |XX     G 123    |
    |3XXXXXXXXXXXXXX |
    |  F             |
    |          F     |
    +----------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def test14():
    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


def test15():
    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """

    map_graph = RoutingGraph(map_str)
    # changing the heuristic so the search behaves like LCFS
    map_graph.estimated_cost_to_goal = lambda node: 0

    frontier = AStarFrontier(map_graph)

    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


def test16():
    map_str = """\
    +-------------+
    | G         G |
    |      S      |
    | G         G |
    +-------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


def test17():
    map_str = """\
        +-------+
        |     XG|
        |X XXX  |
        |  S    |
        +-------+
        """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


def test18():
    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


def test19():
    map_str = """\
    +----+
    |    |
    | SX |
    | X G|
    +----+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


def test20():
    map_str = """\
    +---------------+
    |    G          |
    |XXXXXXXXXXXX   |
    |           X   |
    |  XXXXXX   X   |
    |  X S  X   X   |
    |  X        X   |
    |  XXXXXXXXXX   |
    |               |
    +---------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

def test21():
    map_str = """\
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


def q1():
    test1()
    test2()
    test3()
    test4()


def q2():
    test5()
    test6()
    test7()
    test9()
    test10()
    test11()
    test12()
    test8()
    test13()


def q3():
    test14()
    test15()
    test16()
    test17()
    test18()
    test19()
    test20()
    test21()