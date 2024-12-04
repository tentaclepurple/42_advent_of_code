def read_grid(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f if line.strip()]


def check_pattern(grid, row, col):
    """Check if there's an X-MAS pattern starting at the given center position"""
    height = len(grid)
    width = len(grid[0])
    
    # Check if room
    if (row == 0 or row >= height - 1 or 
        col == 0 or col >= width - 1):
        return False
    
    mas_patterns = ["MAS", "SAM"]
    
    # For each diagonal pair
    for p1 in mas_patterns:
        for p2 in mas_patterns:
            # Check top-left to bottom-right diagonal
            tl_valid = (
                grid[row-1][col-1] == p1[0] and
                grid[row][col] == p1[1] and
                grid[row+1][col+1] == p1[2]
            )
            
            # Check top-right to bottom-left diagonal
            tr_valid = (
                grid[row-1][col+1] == p2[0] and
                grid[row][col] == p2[1] and
                grid[row+1][col-1] == p2[2]
            )
            
            if tl_valid and tr_valid:
                return True
    
    return False


def count_xmas(grid):
    count = 0
    height = len(grid)
    width = len(grid[0])
    
    # Check center of the X (A)
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if check_pattern(grid, row, col):
                count += 1
    
    return count


if __name__ == "__main__":
    grid = read_grid('input.txt')
    result = count_xmas(grid)
    print(f"{result} occurrences of XMAS")
