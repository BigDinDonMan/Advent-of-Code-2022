from __future__ import annotations
from dataclasses import dataclass, field
from typing import Tuple, List
import numpy as np
from queue import PriorityQueue

with open('input.txt', mode='r') as f:
    file_lines = f.readlines()

@dataclass
class Node:
    symbol: str
    height: int
    position: Tuple[int, int]
    neighbours: List[Node] = field(default_factory=list, repr=False)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.position == other.position
    
    def __hash__(self) -> int:
        return hash(self.position)

    def __lt__(self, other):
        return self.position < other.position

    def __gt__(self, other):
        return self.position > other.position

class AStarSolver:
    def __init__(self, graph):
        self.graph = graph

    def run(self, start: Node, end: Node) -> Tuple[dict, bool]:
        queue = PriorityQueue()
        queue.put((0, start))
        scores = { start: 0 }
        came_from = { start: None }

        success = False

        while queue.qsize() > 0:
            current = queue.get()[1]

            if current == end:
                success = True
                break

            for node in current.neighbours:
                new_cost = scores[current] + 1
                if node not in scores or new_cost < scores[node]:
                    scores[node] = new_cost
                    priority = new_cost + self.__heuristic(node, end)
                    queue.put((priority, node))
                    came_from[node] = current

        return self.__reconstruct_path(came_from, end), success

    def __reconstruct_path(self, came_from, dest):
        current = dest
        path = [dest]
        while current is not None:
            new = came_from.get(current)
            if new is not None:
                path.append(new)
            current = new
        return path
    
    def __heuristic(self, n1: Node, n2: Node) -> float:
        return abs(n1.position[0] - n2.position[0]) + abs(n1.position[1]-n2.position[1])

def init_height_map():
    m = {}
    for i in range(ord('a'), ord('z')+1):
        m[chr(i)] = i
    m['S'] = m['a']
    m['E'] = m['z']
    return m

def build_graph(lines, height_map) -> List[Node]:
    nodes = []
    for i, val in enumerate(lines):
        row = []
        for j, val2 in enumerate(val.strip()):
            row.append(Node(val2, height_map[val2], (j, i)))
        nodes.append(row)
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            node = nodes[i][j]
            if (i > 0) and (nodes[i-1][j].height - node.height <= 1):
                node.neighbours += [nodes[i-1][j]]
            if (i < len(nodes) - 1)  and (nodes[i+1][j].height - node.height <= 1): 
                node.neighbours += [nodes[i+1][j]]
            if (j > 0)  and (nodes[i][j-1].height - node.height <= 1): 
                node.neighbours += [nodes[i][j-1]]
            if (j < len(nodes[i]) - 1) and (nodes[i][j+1].height - node.height <= 1):
                node.neighbours += [nodes[i][j+1]]

    return np.array(nodes).flatten().tolist()

def run_solution(graph):
    start_node = next(x for x in graph if x.symbol == 'S')
    dest_node = next(x for x in graph if x.symbol == 'E')
    path, _ = AStarSolver(graph).run(start_node, dest_node)
    print(f"Result: {len(path) - 1}") 

def run_solution_2(graph):
    start_nodes = [x for x in graph if x.symbol == 'S' or x.symbol == 'a']
    dest_node = next(x for x in graph if x.symbol == 'E')
    solver = AStarSolver(graph)
    results = [solver.run(node, dest_node) for node in start_nodes]
    results = [r for r in results if r[1] == True]
    print(f"Result: {min(len(r[0]) for r in results) - 1}")

height_map = init_height_map()
graph = build_graph(file_lines, height_map)

run_solution(graph)
run_solution_2(graph)