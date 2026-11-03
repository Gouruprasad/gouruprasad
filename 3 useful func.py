def find_max(values):
    """Return the maximum value in a list of numbers."""
    highest = values[0]
    for v in values:
        if v > highest:
            highest = v
    return highest

def count_occurrences(items, target):
    """Count how many times target appears in items."""
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

def filter_by_value(d, minimum):
    """Return a new dict with only the key-value pairs where value >= minimum."""
    filtered = {}
    for key, value in d.items():
        if value >= minimum:
            filtered[key] = value
    return filtered
print(find_max([4, 9, 2]))                               
print(count_occurrences(["a", "b", "a", "a"], "a"))      
print(filter_by_value({"Ana": 15, "Ben": 9}, 10))        
