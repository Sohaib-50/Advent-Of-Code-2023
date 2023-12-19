with open("test_case.txt") as f:
    data = f.read().split("\n\n")

workflows = {workflow[:workflow.find("{")]: workflow[workflow.find("{"):][1:-1].split(",") for workflow in data[0].split("\n")}
parts = data[1].split("\n")
parts = [{x[0]: int(x[2:]) for x in part[1:-1].split(",")} for part in parts]

class Node:
    def __init__(self, condition, workflow, target_workflow, parent=None):
        self.condition = condition
        self.workflow = workflow
        self.target_workflow = target_workflow
        self.parent = parent
    
    def __str__(self):
        return f"Cond: {self.condition}, from: {self.workflow}, to: {self.target_workflow}, parent: {self.parent.condition}"

    def __repr__(self) -> str:
        return self.__str__()

frontier = []
for rule in workflows["in"]:
    rule = rule.split(":")
    if len(rule) == 2:
        frontier.append(Node(condition=rule[0], workflow="in", target_workflow=rule[1]))
    else:
        frontier.append(Node(condition="", workflow="in", target_workflow=rule[0]))


accepted_nodes = []
while frontier:

    current_node = frontier.pop(0)
    target = current_node.target_workflow

    # goal test
    if target == "A":
        accepted_nodes.append(current_node)
        continue
    if target == "R":
        continue

    # expand node
    for rule in workflows[target]:
        rule = rule.split(":")
        if len(rule) == 2:
            frontier.append(
                Node(condition=rule[0], workflow=target, 
                     target_workflow=rule[1], parent=current_node)
            )
        else:
            frontier.append(
                Node(condition="", workflow=target, 
                     target_workflow=rule[0], parent=current_node)
            )

accepted_paths = []
for node in accepted_nodes:
    path = []
    current = node
    while current.parent:
        path.append(current)
        current = current.parent
    path.append(current)
    path.reverse()
    accepted_paths.append(path)

combinations = {
    "x": range(1, 4001),
    "m": range(1, 4001),
    "a": range(1, 4001),
    "s": range(1, 4001)
}

# combinations_count = 1
# for key in combinations:
#     combinations_count *= len(combinations[key])
# print(combinations_count)


accepted_combinations = []
for path in accepted_paths:
    combinations = {
        "x": range(1, 4001),
        "m": range(1, 4001),
        "a": range(1, 4001),
        "s": range(1, 4001)
    }

    for node in path:
        condition = node.condition if node.condition else 'default'
        # print(f"{node.workflow}({condition})", end=" -> ")
        if condition != "default":
            target_variable = condition[0]
            current_range = combinations[target_variable]
            new_range = list(filter( eval(f"lambda {target_variable}: {condition}"), current_range)) 
            combinations[target_variable] = new_range  
    accepted_combinations.append(combinations)      
            
final_combinations = {
    "x": set(),
    "m": set(),
    "a": set(),
    "s": set()
}
for combo in accepted_combinations:
    for key in combo:
        # print(f"{key}: {len(combo[key])}")  
        # intersection
        final_combinations[key] = final_combinations[key].union(combo[key])
    # print()
        
for key in final_combinations:
    print(f"{key}: {len(final_combinations[key])}")