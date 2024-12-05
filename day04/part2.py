from collections import defaultdict, deque

def read_input(filename):
    rules = defaultdict(set)
    updates = []
    reading_rules = True
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                reading_rules = False
                continue
                
            if reading_rules:
                before, after = line.split('|')
                rules[before].add(after)
            else:
                update = line.split(',')
                updates.append(update)
    
    return rules, updates

def is_valid_order(pages, rules):
    page_positions = {page: i for i, page in enumerate(pages)}
    
    for before_page in rules:
        if before_page in page_positions:
            before_pos = page_positions[before_page]
            for after_page in rules[before_page]:
                if after_page in page_positions:
                    after_pos = page_positions[after_page]
                    if before_pos >= after_pos:
                        return False
    return True

def build_graph(pages, rules):
    """Build a graph for the given pages based on the rules."""
    # Create adjacency lists and track incoming edges
    graph = defaultdict(set)
    in_degree = {page: 0 for page in pages}
    
    # Add edges based on rules
    for before_page in rules:
        if before_page in pages:
            for after_page in rules[before_page]:
                if after_page in pages:
                    graph[before_page].add(after_page)
                    in_degree[after_page] += 1
    
    return graph, in_degree

def topological_sort(pages, rules):
    """Order pages according to rules using Kahn's algorithm."""
    # Build the graph
    graph, in_degree = build_graph(pages, rules)
    
    # Initialize queue with nodes that have no incoming edges
    queue = deque([page for page in pages if in_degree[page] == 0])
    result = []
    
    # Process nodes
    while queue:
        current = queue.popleft()
        result.append(current)
        
        # Remove edges from current node
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

def get_middle_page(pages):
    middle_idx = len(pages) // 2
    return pages[middle_idx]

def solve_part_two(filename):
    rules, updates = read_input(filename)
    middle_sum = 0
    
    for update in updates:
        if not is_valid_order(update, rules):
            # Order this invalid update
            ordered_update = topological_sort(update, rules)
            middle_page = get_middle_page(ordered_update)
            print(f"Invalid update: {','.join(update)}")
            print(f"Ordered update: {','.join(ordered_update)}")
            print(f"Middle page: {middle_page}")
            middle_sum += int(middle_page)
    
    return middle_sum


if __name__ == '__main__':
    result = solve_part_two('input.txt')
    print(f"\nSum of middle pages from corrected invalid updates: {result}")