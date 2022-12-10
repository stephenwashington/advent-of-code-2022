# part 1: rope of length 1
import math
class Motion:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = int(distance)

class Rope:
    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]

    def update_head_position(self, motion):
        if motion.direction == "U":
            self.head[0] -= 1
        elif motion.direction == "D":
            self.head[0] += 1
        elif motion.direction == "L":
            self.head[1] -= 1
        elif motion.direction == "R":
            self.head[1] += 1

        self.update_tail_position()

    def update_tail_position(self):
        self.head[0] = self.head[0]
        self.head[1] = self.head[1]
        self.tail[0] = self.tail[0]
        self.tail[1] = self.tail[1]
        row_distance = abs(self.head[0] - self.tail[0])
        col_distance = abs(self.head[1] - self.tail[1])
        if row_distance == 2 or col_distance == 2: # head and tail are two rows apart
            if self.head[1] > self.tail[1]: # head is to the right of tail
                self.tail[1] += 1
            elif self.head[1] < self.tail[1]: # head is to the left of tail
                self.tail[1] -= 1

            if self.head[0] > self.tail[0]: # head is below tail
                self.tail[0] += 1 # move tail one row down
            elif self.head[0] < self.tail[0]: # head is above tail
                self.tail[0] -= 1 # move tail one row up

motion_list = []
with open("input.txt") as f:  
    for line in f:
        l = line.strip().split(" ")
        new_motion = Motion(l[0], int(l[1]))
        motion_list.append(new_motion)


tail_location_set = set()
rope = Rope()

for motion in motion_list:
    for _ in range(motion.distance):
        rope.update_head_position(motion)
        tail_location_set.add((rope.tail[0], rope.tail[1]))

visited_spaces = len(list(tail_location_set))
print(visited_spaces)