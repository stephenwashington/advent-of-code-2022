class Range:
    def __init__(self, bounds):
        self.lower = int(bounds[0])
        self.upper = int(bounds[1])

def is_in_bounds(left, right):
    return left.lower >= right.lower and left.upper <= right.upper

def overlaps(left, right):
    return left.lower <= right.lower <= left.upper

contains_count = 0
overlaps_count = 0

with open("input.txt") as f:
    for line in f:
        left_range, right_range = line.strip().split(",")
        left = Range(left_range.split("-"))
        right = Range(right_range.split("-"))

        if is_in_bounds(left, right) or is_in_bounds(right, left):
            contains_count += 1
        if overlaps(left, right) or overlaps(right, left):
            overlaps_count += 1

# Part 1: number of pairs where one range contains another
print(contains_count)

# Part 2: number of pairs where they overlap
print(overlaps_count)
