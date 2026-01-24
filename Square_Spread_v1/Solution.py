def boundary_coordinates(start_point, spread):
    x0, y0 = start_point
    coords = set()
    # Top and bottom edges
    for x in range(x0 - spread, x0 + spread + 1):
        coords.add((x, y0 + spread))  # top edge
        coords.add((x, y0 - spread))  # bottom edge
    # Left and right edges (excluding corners to avoid duplicates)
    for y in range(y0 - spread + 1, y0 + spread):
        coords.add((x0 - spread, y))  # left edge
        coords.add((x0 + spread, y))  # right edge
    return coords



# Test case 1:
start_point = (0, 0)
spread = 2
print(boundary_coordinates(start_point, spread))

# Test Case 2
print(boundary_coordinates(start_point = (3, 4), spread = 1))

# # Test Case 3
print(boundary_coordinates(start_point = (-1, -1), spread = 3))

# # Test Case 4
print(boundary_coordinates(start_point = (5, -3), spread = 0))
