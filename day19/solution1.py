with open("input.txt") as f:
    data = f.read().split("\n\n")

workflows = {workflow[:workflow.find("{")]: workflow[workflow.find("{"):][1:-1].split(",") for workflow in data[0].split("\n")}
parts = data[1].split("\n")
parts = [{x[0]: int(x[2:]) for x in part[1:-1].split(",")} for part in parts]

# print(workflows)
accepted_indices = []
for i, part in enumerate(parts):
    # print(f"part: {part}")
    x = part["x"]
    m = part["m"]
    a = part["a"]
    s = part["s"]
    goto = "in"
    while goto not in ("A", "R"):
        workflow = workflows[goto]
        # print(workflow)
        for rule in workflow[:-1]:
            condition, next_workflow = rule.split(":")
            if eval(condition) == True:
                goto = next_workflow
                break
        else:
            goto = workflow[-1]
        
        # print(goto)


    if goto == "A":
        # print("Accepted\n")
        accepted_indices.append(i)
    # else:
    #     print("Rejected\n")

ans = 0
for i in accepted_indices:
    ans += sum(parts[i].values())

print(ans)