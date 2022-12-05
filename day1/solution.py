calories = []

with open("input.txt") as f:
    c = []
    for line in f:
        if line != '\n':
            calorie_count = int(line.strip())
            c.append(calorie_count)
        else:
            calories.append(c)
            c = []

# Solution for part 1 - highest total calorie count
print(max([sum(x) for x in calories]))

# Solution for part 2 - sum of top three of highest calorie count
calorie_sums = sorted([sum(x) for x in calories])
print(sum(calorie_sums[-3:]))
