# part 2: rope of length 10
import math
class Motion:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = int(distance)

    def __str__(self):
        return f"{self.direction} {self.distance}"
    
class Rope:
    def __init__(self, row_init, col_init, rope_length):
        # Do this instead of [[]] * 10 because otherwise all lists are identical in memory
        self.rope_positions = [[row_init, col_init] for _ in range(rope_length)]

    def update_head(self, motion):
        if motion.direction == "U":
            self.rope_positions[0][0] -= 1
        elif motion.direction == "D":
            self.rope_positions[0][0] += 1
        elif motion.direction == "L":
            self.rope_positions[0][1] -= 1
        elif motion.direction == "R":
            self.rope_positions[0][1] += 1

        self.update_rope_positions()
    
    def update_rope_positions(self):
        # slicing off the first one since we already updated the head
        for head_knot_idx, tail_knot in enumerate(self.rope_positions[1:]):
            head_knot = self.rope_positions[head_knot_idx]
            tail_knot = self.update_knot_position(head_knot, tail_knot)

    def tail_position(self):
        return self.rope_positions[-1][0], self.rope_positions[-1][1]

    def update_knot_position(self, head_knot, tail_knot):
        row_distance = abs(head_knot[0] - tail_knot[0])
        col_distance = abs(head_knot[1] - tail_knot[1])
        if row_distance == 2 or col_distance == 2: # head and tail are two rows apart
            if head_knot[1] > tail_knot[1]: # head is to the right of tail
                tail_knot[1] += 1
            elif head_knot[1] < tail_knot[1]: # head is to the left of tail
                tail_knot[1] -= 1

            if head_knot[0] > tail_knot[0]: # head is below tail
                tail_knot[0] += 1 # move tail one row down
            elif head_knot[0] < tail_knot[0]: # head is above tail
                tail_knot[0] -= 1 # move tail one row up
        return tail_knot

motion_list = []
with open("input.txt") as f:  
    for line in f:
        l = line.strip().split(" ")
        new_motion = Motion(l[0], int(l[1]))
        motion_list.append(new_motion)

tail_location_set = set()

rope = Rope(0, 0, 10)
for motion in motion_list:
    for _ in range(motion.distance):
        rope.update_head(motion)
        
        tail_row_idx, tail_col_idx = rope.tail_position()
        tail_location_set.add((tail_row_idx, tail_col_idx))

visited_spaces = len(list(tail_location_set))
print(visited_spaces)