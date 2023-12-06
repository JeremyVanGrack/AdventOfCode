import math as m, re

INPUT_FILE = "Inputs/Day3_Input.txt"

def gears(board):
    chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

    for r, row in enumerate(board):
        for n in re.finditer(r'\d+', row):
            edge = {(r, c) for r in (r-1, r, r+1) for c in range(n.start()-1, n.end()+1)}

            for o in edge & chars.keys():
                chars[o].append(int(n.group()))

    print("Part1:", sum(sum(p)    for p in chars.values()), 
          "\nPart2:", sum(m.prod(p) for p in chars.values() if len(p)==2))

def main():
    f = open(INPUT_FILE, "r")
    board = f.readlines()
    gears(board)

if __name__ == "__main__":
    main()