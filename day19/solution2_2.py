from math import prod


with open("test_case.txt") as f:
    data = f.read().split("\n\n")

workflows = {workflow[:workflow.find("{")]: workflow[workflow.find("{"):][1:-1].split(",") for workflow in data[0].split("\n")}

class Node:
    def __init__(self, condition, workflow, target_workflow, parent=None):
        self.condition = condition
        self.workflow = workflow
        self.target_workflow = target_workflow
        self.parent = parent
    
    def __repr__(self) -> str:
        return f"<Cond: ({self.condition}), from: {self.workflow}, to: {self.target_workflow}, parent: {self.parent.condition if self.parent is not None else None}>"


frontier = []
temp_node = None
workflow = "in"
for rule in workflows[workflow]:
    rule = rule.split(":")
    if len(rule) == 2:
        new_node = Node(condition=rule[0], workflow=workflow, target_workflow=rule[1], parent=temp_node)
    else:
        new_node = Node(condition="", workflow=workflow, target_workflow=rule[0], parent=temp_node)
    frontier.append(new_node)
    temp_node = new_node


accepted_nodes = []
while frontier:

    current_node = frontier.pop(0)
    target = current_node.target_workflow

    # goal tests
    if target == "A":  # accept
        accepted_nodes.append(current_node)
        continue
    if target == "R":  # reject
        continue

    # expand node
    temp_node = current_node
    for rule in workflows[target]:
        rule = rule.split(":")
        if len(rule) == 2:
            new_node = Node(condition=rule[0], workflow=target, target_workflow=rule[1], parent=temp_node)
        else:
            new_node = Node(condition="", workflow=workflow, target_workflow=rule[0], parent=temp_node)
        frontier.append(new_node)


accepted_combinations = []
for node in accepted_nodes:
    combinations = {
        "x": range(1, 4001),
        "m": range(1, 4001),
        "a": range(1, 4001),
        "s": range(1, 4001)
    }
    current = node
    while current:
        condition = current.condition

        if condition:
            condition_var = condition[0]
            current_range = combinations[condition_var]
            new_range = list(filter( eval(f"lambda {condition_var}: {condition}"), current_range)) 
            combinations[condition_var] = new_range  

        current = current.parent
    
    accepted_combinations.append(combinations)

accepted = 0
for x in range(1, 4001):
    for m in range(1, 4001):
        for a in range(1, 4001):
            for s in range(1, 4001):
                print(x, m, a, s)



print(accepted)