crate_stacks = [
    ['W', 'D', 'G', 'B', 'H', 'R', 'V'],
    ['J', 'N', 'G', 'C', 'R', 'F'],
    ['L', 'S', 'F', 'H', 'D', 'N', 'J'],
    ['J', 'D', 'S', 'V'],
    ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
    ['P', 'G', 'H', 'C', 'M'],
    ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
    ['S', 'J', 'R'],
    ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M'],
]

def print_stacks(stacks):
    for stack in stacks:
        print(stack)
    print() 

print_stacks(crate_stacks)
with open('input.txt') as f:
    for line in f:
        print(line)
        l = line.strip().split(' ')
        amount_to_move = int(l[1])
        start_stack_idx = int(l[3]) - 1
        start_stack = crate_stacks[start_stack_idx]
        end_stack_idx = int(l[5]) -1
        end_stack = crate_stacks[end_stack_idx]
        crane_load = []
        for _ in range(amount_to_move):
            crane_load.append(start_stack.pop())
        end_stack.extend(crane_load)
        print_stacks(crate_stacks)

top_crates = ""
for stack in crate_stacks:
    top_crates += stack[-1]

# part one: what crate is at the top of each stack?
print(top_crates)

# part 2: move multiple crates at once
crate_stacks = [
    ['W', 'D', 'G', 'B', 'H', 'R', 'V'],
    ['J', 'N', 'G', 'C', 'R', 'F'],
    ['L', 'S', 'F', 'H', 'D', 'N', 'J'],
    ['J', 'D', 'S', 'V'],
    ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
    ['P', 'G', 'H', 'C', 'M'],
    ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
    ['S', 'J', 'R'],
    ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M'],
]
print_stacks(crate_stacks)
with open('input.txt') as f:
    for line in f:
        print(line)
        l = line.strip().split(' ')
        amount_to_move = int(l[1])
        start_stack_idx = int(l[3]) - 1
        start_stack = crate_stacks[start_stack_idx]
        end_stack_idx = int(l[5]) -1
        end_stack = crate_stacks[end_stack_idx]
        crane_load = []
        for _ in range(amount_to_move):
            crane_load.append(start_stack.pop())
        # to move multiple crates at once, reverse the crate list you move
        end_stack.extend(crane_load[::-1])
        print_stacks(crate_stacks)

top_crates = ""
for stack in crate_stacks:
    top_crates += stack[-1]

# part two: what crate is at the top of each stack?
print(top_crates)