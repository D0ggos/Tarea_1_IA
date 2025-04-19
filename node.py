from dataclasses import dataclass

@dataclass
class Node:
    value : int
    x : int
    y : int
    neighbors : list