def update_current_direction(current_dir, turn):
    directions = ["N", "E", "S", "W"]
    current_idx = directions.index(current_dir)
    if turn == "L":
        new_idx = (current_idx - 1) % 4
    elif turn == "R":
        new_idx = (current_idx + 1) % 4
    return directions[new_idx]

def main(inputs):
    x, y = 0, 0
    engine_state = 0  # 0: Stopped, 1: Started
    curr_dir = "N"    # Initial direction: North
    
    for cmd in inputs:
        if isinstance(cmd, str) and cmd.upper() in ["E", "S"]:
            engine_state = 1 if cmd.upper() == "E" else 0
        elif isinstance(cmd, str) and cmd.upper() in ["L", "R"]:
            curr_dir = update_current_direction(curr_dir, cmd.upper())
        elif isinstance(cmd, int) or (isinstance(cmd, str) and cmd.isdigit()):
            if engine_state == 1:
                distance = int(cmd)
                if curr_dir == "N":
                    y += distance
                elif curr_dir == "S":
                    y -= distance
                elif curr_dir == "E":
                    x += distance
                elif curr_dir == "W":
                    x -= distance
    return [x, y]

# Test Case 1
inp1 = [2, "L", 2, "E", 3]
print(main(inputs=inp1))  # Output: (-3, 0)

# Test Case 2
inp2 = ["E", 2, "R", 3, "S", 4, "L", 1]
print(main(inputs=inp2))  # Output: (3, 2)

print(main(["E", 5, "R", 3, "L", 2, "S", 4, "E", 1]))  # [3, 8]
print(main(["L", "R", 2, "S", 5]))                     # [0, 0]
print(main(["E", 2, "S", 3, "E", 4]))                  # [0, 6]
print(main(["E", 1, "R", 1, "R", 1, "R", 1]))          # [0, 0]
print(main(["X", -1, 0, "e", "l", 2]))                 # [-2, 0]
print(main(["E", "2", "R", 3, "S", "1"]))              # [3, 2]