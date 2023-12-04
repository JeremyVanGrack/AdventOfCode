import re

INPUT_FILE = "Inputs/Day3_Input.txt"
special_characters = "!#$%&'()*+,-/:;<=>?@[\]^_`{|}~"

def recurseRight(line, charIdx):
    num = line[charIdx]
    if (charIdx < len(line) - 1) and (line[charIdx + 1].isdigit()):    
        num = "".join([num, recurseRight(line, charIdx + 1)])
    else:
        return num
    
    return num

def recurseLeft(line, charIdx):
    num = line[charIdx]
    if (charIdx > 0) and (line[charIdx - 1].isdigit()):      
        num = "".join([recurseLeft(line, charIdx - 1), num])
    else:
        return num
    
    return num

# recurse left and right to grab the entire number
def parseNum(lineIdx, charIdx, board):
    if (charIdx > 0) and (board[lineIdx][charIdx - 1].isdigit()):
        num_l = recurseLeft(board[lineIdx], charIdx - 1)
    else:
        num_l = None

    if (charIdx < len(board[lineIdx]) - 1) and (board[lineIdx][charIdx + 1].isdigit()):
        num_r = recurseRight(board[lineIdx], charIdx + 1)
    else:
        num_r = None

    num = [num_l, board[lineIdx][charIdx], num_r]
    num = "".join(item for item in num if item)
    return int(num)

# look at spaces adjacent to a symbol searching
# for numbers
def lookAdjacent(lineIdx, charIdx, board):
    numbers = []
    #look up, up left, up right 
    if((board[lineIdx-1][charIdx-1]).isdigit()):
        recurseNum = parseNum(lineIdx-1, charIdx-1, board)
        if recurseNum not in numbers:
            numbers.append(recurseNum)
    if((board[lineIdx-1][charIdx]).isdigit()):
       recurseNum = parseNum(lineIdx-1, charIdx, board)
       if recurseNum not in numbers:
            numbers.append(recurseNum)
    if((board[lineIdx-1][charIdx+1]).isdigit()):
        recurseNum = parseNum(lineIdx-1, charIdx+1, board)
        if recurseNum not in numbers:
            numbers.append(recurseNum)

    #look left, look right
    if((board[lineIdx][charIdx-1]).isdigit()):
        recurseNum = parseNum(lineIdx, charIdx-1, board)
        if recurseNum not in numbers:
            numbers.append(recurseNum)
    if((board[lineIdx][charIdx+1]).isdigit()):
        recurseNum = parseNum(lineIdx, charIdx+1, board)
        if recurseNum not in numbers:
            numbers.append(recurseNum)

    #look down, down left, down right
    if((board[lineIdx+1][charIdx-1]).isdigit()):
       recurseNum = parseNum(lineIdx+1, charIdx-1, board)
       if recurseNum not in numbers:
            numbers.append(recurseNum)
    if((board[lineIdx+1][charIdx]).isdigit()):
        recurseNum = parseNum(lineIdx+1, charIdx, board)
        if recurseNum not in numbers:
            numbers.append(recurseNum)
    if((board[lineIdx+1][charIdx+1]).isdigit()):
        recurseNum = parseNum(lineIdx+1, charIdx+1, board)
        if recurseNum not in numbers:
            numbers.append(recurseNum)

    # print(lineIdx, charIdx, board[lineIdx][charIdx], numbers)
    return numbers

# def lookAdjacent(idx, line, board):
    # print(idx, line)
    # if line > 0 and line < len(board) - 1:
    #     for c in board[line-1][idx[1]:idx[2]]:
    #         if c not in special_characters:
    #             return True
    #     for c in board[line][idx[1]:idx[2]]:
    #         if c not in special_characters:
    #             return True
    #     for c in board[line+1][idx[1]:idx[2]]:
    #         if c not in special_characters:
    #             return True
    
    # return False

# parse the list and do work every time you come
# across a symbol
def parseBoard(board):
    print("parsing")
    ans = 0
    for lineIdx, line in enumerate(board):
        for charIdx, c in enumerate(line):
            if c in special_characters:
                print(lineIdx, charIdx, c)
                try:
                    Gears.append(sum(lookAdjacent(lineIdx, charIdx, board)))
                except:
                    Gears = [sum(lookAdjacent(lineIdx, charIdx, board))]
    print(sum(Gears))
    # print(board)
    # for idx in indexes:
    #     print(idx)
    # print(ans)

def main():
    f = open(INPUT_FILE, "r")
    board = f.readlines()
    parseBoard(board)

if __name__ == "__main__":
    main()

# to parse by number
# def parseBoard(board):
#     print("parsing")
#     ans = 0
#     for lineIdx, line in enumerate(board):
        # pattern = r'[0-9]+'
        # indexes = [(m.group(), m.start()-1, m.end()+1) for m in re.finditer(pattern, line)]
        # for idx in indexes:
        #     if lookAdjacent(idx, lineIdx, board):
        #         print("adding")
        #         ans += int(idx[0])