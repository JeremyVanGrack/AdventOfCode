import numpy as np
#2075724809 too high, 989384392 too low
INPUT_FILE = "Inputs/Day9_Input.txt"

def getDiff(arr):
    return [(int(j)-int(i)) for i, j in zip(arr[:-1], arr[1:])]

def readSequences(lines):
    ans = 0
    for line in lines:
        line = line.split()
        memo = {}
        k = 0
        diff = getDiff(line)
        while True:
            if (sum(diff) == 0):
                break
            else:
                memo[k] = diff
                diff = getDiff(memo[k])

            k += 1
            
        for key in range(len((memo.keys())) - 1, 0, -1):
            memo[key - 1].append(memo[key][len(memo[key]) - 1] + memo[ key - 1 ][ len( memo[key - 1] ) - 1 ])
            
        line.append(memo[0][len(memo[0]) - 1] + int(line[len(line)-1]))
        ans += line[len(line) - 1]
    print(ans)


def main():
    f = open(INPUT_FILE, "r")
    input = f.readlines()
    readSequences(input)

if __name__ == "__main__":
    main()