def update_direction(current_dir, turn):
    directions = ["N", "E", "S", "W"]
    idx = directions.index(current_dir)
    if turn == "L":
        return directions[(idx - 1) % 4]
    return current_dir  # "R" is now reverse, not turn right

def main_v2(commands):
    x, y = 0, 0
    direction = "N"
    engine_on = False
    reverse_mode = False

    for cmd in commands:
        if isinstance(cmd, str):
            cmd = cmd.upper()
            if cmd == "E":
                engine_on = True
            elif cmd == "S":
                engine_on = False
                reverse_mode = False  # Reset reverse if engine stops
            elif cmd == "L":
                direction = update_direction(direction, "L")
            elif cmd == "R" and engine_on:
                reverse_mode = not reverse_mode  # Toggle reverse mode
        elif isinstance(cmd, int):
            if engine_on:
                distance = cmd
                if reverse_mode:
                    distance *= -1  # Reverse movement direction
                if direction == "N":
                    y += distance
                elif direction == "S":
                    y -= distance
                elif direction == "E":
                    x += distance
                elif direction == "W":
                    x -= distance
    return [x, y]

# Test Cases
print(main_v2(["E", 2, "R", 3]))            # [0, -1]
print(main_v2(["E", -2, "L", -3]))          # [3, -2]
print(main_v2(["E", "R", -4, "R", -1]))     # [0, 3]
print(main_v2(["R", "E", 2, "S", "R", 3]))  # [0, 2]
