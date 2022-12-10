class Instruction:
    def __init__(self, command, argument):
        self.command = command
        self.argument = argument

    def __repr__(self):
        return f"{self.command} {self.argument}"

def draw_pixel(screen, cycle_count, sprite_middle_location):
    row_idx = cycle_count // 40
    col_idx = cycle_count % 40
    if row_idx == 6: # since 240 // 6 == 6 but we want it to be on row 5
        row_idx == 5
    print(cycle_count, row_idx, col_idx, sprite_middle_location)
    if col_idx == sprite_middle_location or \
       col_idx+1 == sprite_middle_location or \
       col_idx-1 == sprite_middle_location:
        screen[row_idx][col_idx] = "#"

instruction_stack = []
with open("input.txt") as f:
    for line in f:
        l = line.strip().split(" ")
        command = l[0]
        argument = int(l[1]) if command == "addx" else None
        new_instruction = Instruction(command, argument)
        instruction_stack.append(new_instruction)

x_register = 1
cycle_count = 0
sprite_middle_location = 1
screen = [["."]*40 for _ in range(6)]

for instruction in instruction_stack:
    if instruction.command == "noop":
        sprite_middle_location = x_register
        draw_pixel(screen, cycle_count, sprite_middle_location)
        cycle_count += 1

    if instruction.command == "addx":
        sprite_middle_location = x_register
        draw_pixel(screen, cycle_count, sprite_middle_location)
        cycle_count += 1

        sprite_middle_location = x_register
        draw_pixel(screen, cycle_count, sprite_middle_location)
        cycle_count += 1
        x_register += instruction.argument
    
for row in screen:
    for pixel in row:
        print(f"{pixel}", end="")
    print()
print()