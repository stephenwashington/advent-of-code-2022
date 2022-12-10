with open("input.txt") as f:
    grid = []
    visibility_grid = []
    for line in f:
        row = []
        visibility_row = []
        for char in line.strip():
            row.append(int(char))
            visibility_row.append(None)
        grid.append(row)
        visibility_grid.append(visibility_row)
    
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            # if it's on an edge, set it to be visible
            if row_idx == 0 or \
               col_idx == 0 or \
               row_idx == len(row)-1 or \
               col_idx == len(grid)-1:
               visibility_grid[row_idx][col_idx] = True
               continue

            tree = grid[row_idx][col_idx]
            # check from the north
            is_visible_north = True
            current_row = row_idx-1
            while current_row >= 0:
                other_tree = grid[current_row][col_idx]
                if other_tree >= tree:
                    is_visible_north = False
                    break
                current_row -= 1
                
            # check from the east
            is_visible_east = True
            current_col = col_idx+1
            while current_col <= len(row)-1:
                other_tree = grid[row_idx][current_col]
                if other_tree >= tree:
                    is_visible_east = False
                    break
                current_col += 1

            # check from the south
            is_visible_south = True
            current_row = row_idx+1
            while current_row <= len(grid)-1:
                other_tree = grid[current_row][col_idx]
                if other_tree >= tree:
                    is_visible_south = False
                    break
                current_row += 1


            # check from the west
            is_visible_west = True
            current_col = col_idx-1
            while current_col >= 0:
                other_tree = grid[row_idx][current_col]
                if other_tree >= tree:
                    is_visible_west = False
                    break
                current_col -= 1

            visibility_grid[row_idx][col_idx] = is_visible_north or is_visible_east or is_visible_south or is_visible_west
            #print(is_visible_north, is_visible_east, is_visible_south, is_visible_west)

    visible_tree_count = sum([sum(row) for row in visibility_grid])
    # Part 1: count all trees visible from at least one edge
    print(visible_tree_count)

with open("input.txt") as f:
    grid = []
    visibility_grid = []
    for line in f:
        row = []
        visibility_row = []
        for char in line.strip():
            row.append(int(char))
            visibility_row.append(None)
        grid.append(row)
        visibility_grid.append(visibility_row)
    
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            # if it's on an edge, set it to be visible
            if row_idx == 0 or \
               col_idx == 0 or \
               row_idx == len(row)-1 or \
               col_idx == len(grid)-1:
               visibility_grid[row_idx][col_idx] = 0
               continue

            visibility_score = 0
            tree = grid[row_idx][col_idx]
            # check from the north
            visible_north_count = 0
            current_row = row_idx-1
            while current_row >= 0:
                other_tree = grid[current_row][col_idx]
                visible_north_count += 1
                if other_tree >= tree:
                    break
                    
                current_row -= 1
                
            # check from the east
            visible_east_count = 0
            current_col = col_idx+1
            while current_col <= len(row)-1:
                other_tree = grid[row_idx][current_col]
                visible_east_count += 1
                if other_tree >= tree:
                    break

                current_col += 1

            # check from the south
            visible_south_count = 0
            current_row = row_idx+1
            while current_row <= len(grid)-1:
                other_tree = grid[current_row][col_idx]
                visible_south_count += 1
                if other_tree >= tree:
                    break
                current_row += 1

            # check from the west
            visible_west_count = 0
            current_col = col_idx-1
            while current_col >= 0:
                other_tree = grid[row_idx][current_col]
                visible_west_count += 1
                if other_tree >= tree:
                    break
                current_col -= 1

            visibility_grid[row_idx][col_idx] = visible_north_count * visible_east_count * visible_south_count * visible_west_count
        
    # part 2: what's the highest scenic score in the entire grid?
    high_score = max([max(row) for row in visibility_grid])
    print(high_score)