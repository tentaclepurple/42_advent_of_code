def is_safe_report(levels):
    if len(levels) < 2:
        return False
        
    diff = levels[1] - levels[0]
    if diff == 0:
        return False
        
    should_increase = diff > 0
    
    for i in range(len(levels)-1):
        diff = levels[i+1] - levels[i]
        
        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if should_increase and diff <= 0:
            return False
        if not should_increase and diff >= 0:
            return False
    
    return True

def is_safe_with_dampener(levels):
    if is_safe_report(levels):
        return True
    
    for i in range(len(levels)):
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe_report(dampened_levels):
            return True
            
    return False

def count_safe_reports(filename):
    safe_count = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            levels = [int(x) for x in line.split()]
            if is_safe_with_dampener(levels):
                safe_count += 1
    return safe_count

if __name__ == '__main__':
    result = count_safe_reports('input.txt')
    print(f"Updated safe reports: {result}")