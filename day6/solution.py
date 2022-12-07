# part 1: start-of-packet marker is first instance of string where last four characters are unique
with open("input.txt") as f:
    buffer = f.readline().strip()
    char_list = ""
    for char in buffer:
        char_list += char
        if len(char_list) >= 4:
            if len(set(char_list[-4:])) == len(char_list[-4:]):
                print(len(char_list))
                break

# part 2: start of message maker is first instance of string where last fourteen characters are unique
with open("input.txt") as f:
    buffer = f.readline().strip()
    char_list = ""
    for char in buffer:
        char_list += char
        if len(char_list) >= 14:
            if len(set(char_list[-14:])) == len(char_list[-14:]):
                print(len(char_list))
                break