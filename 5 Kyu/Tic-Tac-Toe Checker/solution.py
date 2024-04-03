def is_solved(board):
    result = check_line([board[0][0], board[1][1], board[2][2]])
    if result != 0:
        return result
    result = check_line([board[0][2], board[1][1], board[2][0]])
    if result != 0:
        return result
    
    for index, item in enumerate(board[0]):
        column = [board[0][index], board[1][index], board[2][index]]
        result = check_line(column)
        if result != 0:
            return result

    for line in board:
        print(line)
        result = check_line(line)
        if result != 0:
            return result
        
    for line in board:
        if 0 in line:
            return -1
        
    return 0

    
def check_line(line):
    result = 0
    
    if line == [1, 1, 1]:
        result = 1
    
    elif line == [2, 2, 2]:
        result = 2
        
    return result

