# 15Puzzle

The 15-puzzle is a simple sliding puzzle that consists numbered square tiles(in this case 15) in random order with one tile missing.The object of the puzzle is to place the tiles in order by making sliding moves that use the empty space.
The solution is based on the search and util files from here : https://github.com/aimacode/aima-python 

## Use of A* algorithm

A* is an informed search algorithm, or a best-first search, meaning that it solves problems by searching among all possible paths to the solution (goal) for the one that incurs the smallest cost (least distance travelled, shortest time, etc.), and among these paths it first considers the ones that appear to lead most quickly to the solution. It is formulated in terms of weighted graphs: starting from a specific node of a graph, it constructs a tree of paths starting from that node, expanding paths one step at a time, until one of its paths ends at the predetermined goal node.

At each iteration of its main loop, A* needs to determine which of its partial paths to expand into one or more longer paths. It does so based on an estimate of the cost (total weight) still to go to the goal node. Specifically, A* selects the path that minimizes

f(n)=g(n)+h(n)

where n is the last node on the path, g(n) is the cost of the path from the start node to n, and h(n) is a heuristic that estimates the cost of the cheapest path from n to the goal. The heuristic is problem-specific. For the algorithm to find the actual shortest path, the heuristic function must be admissible, meaning that it never overestimates the actual cost to get to the nearest goal node.

Typical implementations of A* use a priority queue to perform the repeated selection of minimum (estimated) cost nodes to expand. This priority queue is known as the open set or fringe. At each step of the algorithm, the node with the lowest f(x) value is removed from the queue, the f and g values of its neighbors are updated accordingly, and these neighbors are added to the queue. The algorithm continues until a goal node has a lower f value than any node in the queue (or until the queue is empty).[a] The f value of the goal is then the length of the shortest path, since h at the goal is zero in an admissible heuristic.

The algorithm described so far gives us only the length of the shortest path. To find the actual sequence of steps, the algorithm can be easily revised so that each node on the path keeps track of its predecessor. After this algorithm is run, the ending node will point to its predecessor, and so on, until some node's predecessor is the start node

As an example, when searching for the shortest route on a map, h(x) might represent the straight-line distance to the goal, since that is physically the smallest possible distance between any two points.



## Heuristic Functions

Three Heuristic Functions were used

* 1.Manhattan Distance
	
	>The distance is calculated as the sum of the absolute differences of their Cartesian coordinates.

* 2.Number of wrong placed pieces/numbers
	
	>The sum of wrongly placed tiles

* 3.Number placed pieces/numbers in wrong column
	
	>The sum of tiles placed in the wrong column


## States
	
Each diffent state of the puzzle is represented by a one dimesnional matrix which consists of 15 ints (0.....14)
0 represents the empty tile



## Actions

The actions specified  are the ones available for the empty tile
1 represents the empty tile to be moved up , 2 down ,3 right ,4 left
For each state a list of actions is returned according to the position of the empty tile
