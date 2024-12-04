def read_grid(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f if line.strip()]


def check_pattern(grid, row, col, dx, dy, pattern):
    # Check if the pattern fits in the grid
    if not (0 <= row + dx*(len(pattern)-1) < len(grid) and 
            0 <= col + dy*(len(pattern)-1) < len(grid[0])):
        return False
        
    for i, char in enumerate(pattern):
        if grid[row + dx*i][col + dy*i] != char:
            return False
    return True


def count_xmas(grid):
    count = 0
    height = len(grid)
    width = len(grid[0])
    pattern = "X-MAS"
    
    directions = [
        (0, 1),   # horizontal right
        (0, -1),  # horizontal left
        (1, 0),   # vertical down
        (-1, 0),  # vertical up
        (1, 1),   # diagonal down-right
        (-1, -1), # diagonal up-left
        (1, -1),  # diagonal down-left
        (-1, 1)   # diagonal up-right
    ]
    
    for row in range(height):
        for col in range(width):
            # Try every direction from this position
            for dx, dy in directions:
                if check_pattern(grid, row, col, dx, dy, pattern):
                    count += 1
                    
    return count


if __name__ == "__main__":
    grid = read_grid('test.txt')
    result = count_xmas(grid)
    print(f"{result} occurrences of XMAS")
