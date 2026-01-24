def all_coordinates(start_point, spread):
    x0, y0 = start_point
    coords = set()
    for x in range(x0 - spread, x0 + spread + 1):
        for y in range(y0 - spread, y0 + spread + 1):
            coords.add((x, y))
    return coords

# Test case 1:
start_point = (0, 0)
spread = 2
print(all_coordinates(start_point, spread))

# Test Case 2
print(all_coordinates(start_point = (3, 4), spread = 1))

# # Test Case 3
print(all_coordinates(start_point = (-1, -1), spread = 3))

# # Test Case 4
print(all_coordinates(start_point = (5, -3), spread = 0))

