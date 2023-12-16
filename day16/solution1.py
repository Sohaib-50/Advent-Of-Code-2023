with open("input.txt") as f:
    grid = f.read().split("\n")

directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}

def is_valid_position(position, grid):
    x, y = position
    return (0 <= x < len(grid)) and (0 <= y < len(grid[0]))

beams = [((0, 0), "right")]
energized = {((0, 0), "right")}
while beams:
    

    pos, direction = beams.pop()
    
    while is_valid_position(pos, grid):
        energized.add((pos, direction))
        x, y = pos
        tile = grid[x][y]

        if tile == ".":
            movement = directions[direction]
            pos = (x + movement[0], y + movement[1])

        elif tile in ("-", "|"):

            if tile == "-":
                if direction in ("right", "left"):
                    movement = directions[direction]
                    pos = (x + movement[0], y + movement[1])
                else:
                    movement0 = directions["right"]
                    movement1 = directions["left"]
                    pos0 = (x + movement0[0], y + movement0[1])
                    pos1 = (x + movement1[0], y + movement1[1])
                    beams.append((pos0, "right"))
                    pos = pos1
                    direction = "left"
            else:  # tile == "|"
                if direction in ("up", "down"):
                    movement = directions[direction]
                    pos = (x + movement[0], y + movement[1])
                else:
                    movement0 = directions["up"]
                    movement1 = directions["down"]
                    pos0 = (x + movement0[0], y + movement0[1])
                    pos1 = (x + movement1[0], y + movement1[1])
                    beams.append((pos0, "up"))
                    pos = pos1
                    direction = "down"

        
        else:  # tile is a mirror
            if tile == "/":
                 #  /: right -> up. left -> down. up -> right. down -> left
                match direction:
                    case "right":
                        direction = "up"
                    case "left":
                        direction = "down"
                    case "up":
                        direction = "right"
                    case "down":
                        direction = "left"

            elif tile == "\\":
                # \: right -> down, left -> up, up -> left down -> right 
                match direction:
                    case "right":
                        direction = "down"
                    case "left":
                        direction = "up"
                    case "up":
                        direction = "left"
                    case "down":
                        direction = "right"
            
            movement = directions[direction]
            pos = (x + movement[0], y + movement[1])

        if (pos, direction) in energized:
            break
        elif is_valid_position(pos, grid):
            energized.add((pos, direction))
            
energized_coordinates = set([pos for pos, direction in energized])
print(len(energized_coordinates))

                        
                

           

            

        
