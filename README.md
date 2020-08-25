# Artificial Intelligence Assignment 1
[![Run on Repl.it](https://repl.it/badge/github/RyBeau/AIAssignment1)](https://repl.it/github/RyBeau/AIAssignment1)

This is the code for the my submission for the first Assignment SuperQuiz for COSC367. For this assignment we were presented
with map that represented a starting position and a goal/goals to get to. We had to write a class to represent these maps
(RoutingGraph) and then an AStar graph search frontier to be used to search the RoutingGraph to find the solution.

## Map String Guide
Below is an example map string.

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

* G represents a goal node.
* S represents a starting node.
* X represent obstacles that must be avoided.
* The border is the bounds of a map.
* Spaces are empty space that can be moved through.

Below is an example of a solution string.

    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |     ...S       |
    |     ...*       |
    |     ...*       |
    |     G***       |
    |                |
    |                |
    |                |
    +----------------+

* . represents a space that has been explored whilst searching for the optimal solution.
* \* Represents a space that is part of the optimal path to the closest goal node.

## Demo
tests.py contains some of the tests from the Quiz Server. To demo this project you can download the repo and run tests.py.
You can also run it online here: 

[![Run on Repl.it](https://repl.it/badge/github/RyBeau/AIAssignment1)](https://repl.it/github/RyBeau/AIAssignment1)

#### Search.py
This was provided during the course an provides various classes and abstract classes related to graphs and graph searching.
It's author is Kourosh Neshatian.
