import heapq
import time

start = time.time()

with open('input.txt') as f:
    grid = f.read().split("\n")

grid = [[int(x) for x in row] for row in grid]



movements = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}

def is_valid_position(position):
    x, y = position
    return (0 <= x < len(grid)) and (0 <= y < len(grid[0]))

class Node:
    def __init__(self, pos, cost, action, steps=1):
        self.pos = pos
        self.cost = cost
        self.action = action
        self.steps = steps
    
    def __str__(self):
        return f"<{self.pos}: {self.cost}>"
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash((self.pos, self.action, self.steps))
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.pos == other.pos and self.action == other.action and self.steps == other.steps
    
    def __lt__(self, other):
        return self.cost < other.cost
    
end_pos = (len(grid) - 1, len(grid[0]) - 1)

frontier = []
heapq.heappush(frontier, Node(pos=(0, 1), cost=grid[0][1], action="right", steps=1))
heapq.heappush(frontier, Node(pos=(1, 0), cost=grid[1][0], action="down", steps=1))

visited = set()

while frontier:
    node = heapq.heappop(frontier)

    if node.pos == end_pos:
        break

    if node in visited:
        continue

    visited.add(node)

    # expand node

    if node.steps != 3:
        action_direction = movements[node.action]
        new_pos = (node.pos[0] + action_direction[0],  node.pos[1] + action_direction[1])
        if is_valid_position(new_pos):
            new_cost = node.cost + grid[new_pos[0]][new_pos[1]]
            heapq.heappush(
                frontier,
                Node(pos=new_pos, cost=new_cost, action=node.action, steps=node.steps + 1)
            )

    if node.action in ("right", "left"):  # "right/left" is up/down
        new_actions = ["up", "down"]
    else:
        new_actions = ["right", "left"]
    for new_action in new_actions:
        action_direction = movements[new_action]
        new_pos = (node.pos[0] + action_direction[0],  node.pos[1] + action_direction[1])
        if is_valid_position(new_pos):
            new_cost = node.cost + grid[new_pos[0]][new_pos[1]]
            heapq.heappush(
                frontier,
                Node(pos=new_pos, cost=new_cost, action=new_action, steps=1)
            )

print(node.cost)

end = time.time()
print(end - start, "seconds")