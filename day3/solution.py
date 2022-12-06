import string
priority_score = 0

with open("input.txt") as f:
    for line in f:
        l = line.strip()
        left_half, right_half = set(l[:len(l)//2]), set(l[len(l)//2:])
        common_char = left_half & right_half
        if list(common_char)[0] in string.ascii_lowercase:
            priority_score += ord(list(common_char)[0]) - 96
        elif list(common_char)[0] in string.ascii_uppercase:
            priority_score += ord(list(common_char)[0]) - 38
# Part 1: What is the sum of the priority of the common rucksack elements?
print(priority_score)

# Part 2: Find the common element and priority sum for groups of three elves
priority_score = 0
set_of_three_elves = []
with open("input.txt") as f:
    elf_set = []
    for line in f:
        elf_set.append(set(line.strip()))
        if len(elf_set) == 3:
            set_of_three_elves.append(elf_set)
            elf_set = []
    for elf_set in set_of_three_elves:
        common_char = elf_set[0] & elf_set[1] & elf_set[2]
        if list(common_char)[0] in string.ascii_lowercase:
            priority_score += ord(list(common_char)[0]) - 96
        elif list(common_char)[0] in string.ascii_uppercase:
            priority_score += ord(list(common_char)[0]) - 38
# Part 1: What is the sum of the priority of the common rucksack elements?
print(priority_score)