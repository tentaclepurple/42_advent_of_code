def read_input(filename):
    rules = {}
    updates = []
    reading_rules = True
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                reading_rules = False
                continue
                
            if reading_rules:
                # Parse rule X|Y: X must come before Y
                before, after = line.split('|')
                if before not in rules:
                    rules[before] = set()
                rules[before].add(after)
            else:
                # Parse update pages
                update = line.split(',')
                updates.append(update)
    
    return rules, updates

def is_valid_order(pages, rules):
    """Check if an update's page order satisfies all applicable rules."""
    # Create index mapping for quick position lookups
    page_positions = {page: i for i, page in enumerate(pages)}
    
    # Check each rule where both pages are in the update
    for before_page in rules:
        if before_page in page_positions:
            before_pos = page_positions[before_page]
            
            for after_page in rules[before_page]:
                if after_page in page_positions:
                    after_pos = page_positions[after_page]
                    
                    # Rule violated if 'before' page comes after 'after' page
                    if before_pos >= after_pos:
                        return False
    
    return True


def get_middle_page(pages):
    """Get the middle page number of an update."""
    middle_idx = len(pages) // 2
    return pages[middle_idx]


def solve_page_ordering(filename):
    rules, updates = read_input(filename)

    print(f"Rules:, {rules}")

    print(f"Updates:, {updates}")
    print()
    
    middle_sum = 0
    for update in updates:
        if is_valid_order(update, rules):
            middle_page = get_middle_page(update)
            print(f"Valid update: {','.join(update)} (middle page: {middle_page})")
            middle_sum += int(middle_page)
        else:
            print(f"Invalid update: {','.join(update)}")
    
    return middle_sum


if __name__ == '__main__':


    result = solve_page_ordering('input.txt')
    print(f"\nSum of middle pages from valid updates: {result}")