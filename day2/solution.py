score = 0

shapes = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

outcomes = {
    "win": 6,
    "draw": 3,
    "lose": 0
}
with open("input.txt") as f:
    for line in f:
        opponent, me = line.strip().split(" ")
        score += shapes[me]
        if opponent == "A" and me == "X": score += outcomes["draw"]
        elif opponent == "A" and me == "Y": score += outcomes["win"]
        elif opponent == "A" and me == "Z": score += outcomes["lose"]
        elif opponent == "B" and me == "X": score += outcomes["lose"]
        elif opponent == "B" and me == "Y": score += outcomes["draw"]
        elif opponent == "B" and me == "Z": score += outcomes["win"]
        elif opponent == "C" and me == "X": score += outcomes["win"]
        elif opponent == "C" and me == "Y": score += outcomes["lose"]
        elif opponent == "C" and me == "Z": score += outcomes["draw"]

# Part 1: Score if you follow the strategy guide perfectly
print(score)

# Part 2: X, Y, Z = win, draw, lose
score = 0
shapes = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

outcome_scores = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

with open("input.txt") as f:
    for line in f:
        opponent, desired_outcome = line.strip().split(" ")
        if opponent == "A" and desired_outcome == "X":  my_shape = "scissors"
        elif opponent == "A" and desired_outcome == "Y": my_shape = "rock"
        elif opponent == "A" and desired_outcome == "Z": my_shape = "paper"
        elif opponent == "B" and desired_outcome == "X": my_shape = "rock"
        elif opponent == "B" and desired_outcome == "Y": my_shape = "paper"
        elif opponent == "B" and desired_outcome == "Z": my_shape = "scissors"
        elif opponent == "C" and desired_outcome == "X": my_shape = "paper"
        elif opponent == "C" and desired_outcome == "Y": my_shape = "scissors"
        elif opponent == "C" and desired_outcome == "Z": my_shape = "rock"
        score += shapes[my_shape]
        score += outcome_scores[desired_outcome]
print(score)