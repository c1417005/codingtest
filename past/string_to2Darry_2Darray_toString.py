input_lines = ["##.", ".#.", "..#"]

grid = [list(row) for row in input_lines]

output = ["".join(row) for row in grid]




print(f"before_grid:{grid}")
print(f"before_output:{output}")

grid[0][0] = "."
grid[0][1] = "."

output = ["".join(row) for row in grid]
print(f"after_grid:{grid}")
print(f"after_output:{output}")
