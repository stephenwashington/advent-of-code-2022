class Instruction:
    def __init__(self, command, argument):
        self.command = command
        self.argument = argument

    def __repr__(self):
        return f"{self.command} {self.argument}"

instruction_stack = []

with open("input.txt") as f:
    for line in f:
        l = line.strip().split(" ")
        command = l[0]
        argument = int(l[1]) if command == "addx" else None
        new_instruction = Instruction(command, argument)
        instruction_stack.append(new_instruction)

x_register = 1
cycle_count = 1
special_cycle_counts = [20, 60, 100, 140, 180, 220]
signal_strength_sum = 0

def check_cycle_count(cycle_count, x_register):
    signal_strength = 0
    if cycle_count in special_cycle_counts:
        print(f"{cycle_count}, {x_register}")
        signal_strength = cycle_count * x_register
    return signal_strength

for instruction in instruction_stack:
    if instruction.command == "noop":
        cycle_count += 1
        signal_strength_sum += check_cycle_count(cycle_count, x_register)
    if instruction.command == "addx":
        cycle_count += 1
        signal_strength_sum += check_cycle_count(cycle_count, x_register)
        cycle_count += 1
        x_register += instruction.argument
        signal_strength_sum += check_cycle_count(cycle_count, x_register)
    
print(signal_strength_sum)