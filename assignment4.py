import sys
health = int(sys.argv[3])


def open_file(filename):   # read file and create 2-D list
    with open(filename) as file:
        path = [i.strip('\n') for i in file]
        outer_list = []
        for x in path:
            inner_list = []
            for cell in x:
                inner_list.append(cell)
            outer_list.append(inner_list)
    return outer_list


def search(row, column, solve_list):  # control situation
    global health
    if row >= len(solve_list) or row < 0 or column < 0 or column >= len(solve_list[0]):
        return False
    elif solve_list[row][column] == 'P':
        health -= 1
        return True
    elif solve_list[row][column] != 'P':
        if solve_list[row][column] == 'H':
            health = int(sys.argv[3])   # update health time
            return True
        elif solve_list[row][column] == 'F':
            health -= 1
            return True
        else:
            return False


def maze(row, column, solve_list):
    if solve_list[row][column] == 'F':  # base case
        return solve_list
    elif search(row - 1, column, solve_list):   # recursion case
        solve_list[row][column] = '1'
        return maze(row-1, column, solve_list)
    elif search(row, column + 1, solve_list):
        solve_list[row][column] = '1'
        return maze(row, column+1, solve_list)
    elif search(row, column - 1, solve_list):
        solve_list[row][column] = '1'
        return maze(row, column-1, solve_list)
    elif search(row + 1, column, solve_list):
        solve_list[row][column] = '1'
        return maze(row+1, column, solve_list)
    elif row + 1 < len(solve_list) and column < len(solve_list[0]) and solve_list[row + 1][column] == '1':
        solve_list[row][column] = '0'    # backtracking
        return maze(row + 1, column, solve_list)
    elif row < len(solve_list) and column + 1 < len(solve_list[0]) and solve_list[row][column + 1] == '1':
        solve_list[row][column] = '0'
        return maze(row, column + 1, solve_list)
    elif row < len(solve_list) and column - 1 < len(solve_list[0]) and solve_list[row][column - 1] == '1':
        solve_list[row][column] = '0'
        return maze(row, column - 1, solve_list)
    elif row - 1 < len(solve_list) and column < len(solve_list[0]) and solve_list[row - 1][column] == '1':
        solve_list[row][column] = '0'
        return maze(row - 1, column, solve_list)


def solve_maze(maze_list):
    global health
    health = int(sys.argv[3])
    row_s, column_s = 0, 0
    for x in range(len(maze_list)):
        for y in range(len(maze_list[0])):
            if maze_list[x][y] == 'S':
                row_s, column_s = x, y   # index of start point
    maze(row_s, column_s, maze_list)  # solve maze
    maze_list[row_s][column_s] = 'S'  # do again start point 'S'
    for x in range(len(maze_list)):  # do zero except F,S,1 cells
        for y in range(len(maze_list[0])):
            if maze_list[x][y] != 'F' and maze_list[x][y] != 'S' and maze_list[x][y] != '1':
                maze_list[x][y] = '0'
    return maze_list


with open(sys.argv[4], "w") as file_t:
    file_t.write("solve maze without health condition\n")
    for a in solve_maze(open_file(sys.argv[1])):
        file_t.writelines(', '.join(a))
        file_t.writelines("\n")
    file_t.write("solve maze with health condition\n")
    for b in solve_maze(open_file(sys.argv[2])):
        file_t.writelines(', '.join(b))
        file_t.writelines("\n")
