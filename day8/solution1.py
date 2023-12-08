file_name = "input.txt"
with open(file=file_name) as f:
    lr_instructions, nodes = f.read().split("\n\n")

nodes = [x for x in nodes.splitlines()]
nodes = [x.split(" = ") for x in nodes]
nodes = {node: neighbors
         for node, neighbors in nodes}

for node in nodes:
    neighbors = nodes[node].split(", ")
    nodes[node] = neighbors[0].strip("("), neighbors[1].strip(")")

current = "AAA"
i = 0
while current != "ZZZ":
    neighbors = nodes[current]
    lr_instruction = lr_instructions[i % len(lr_instructions)] 
    i += 1
    
    if lr_instruction == "L":
        current = neighbors[0]
    else:
        current = neighbors[1]

print(i)