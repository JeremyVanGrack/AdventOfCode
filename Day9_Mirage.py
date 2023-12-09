import numpy as np
#2075724809 too high, 989384392 too low
INPUT_FILE = "Inputs/Day9_Input.txt"

def readSequences(lines):
    ans = 0
    for line in lines:
        line = line.split()
        memo = {}
        arr = [(int(j)-int(i)) for i, j in zip(line[:-1], line[1:])]
        memo[0] = arr[len(arr)-1]
        i = 1
        print(arr)
        while True:

            arr = [(int(j)-int(i)) for i, j in zip(arr[:-1], arr[1:])]
            memo[i] = arr[len(arr)-1]
            i += 1
            print(arr)
            if sum(arr) == 0:
                break

        # print(arr, memo)
        memo.pop(len(memo) - 1)
        arr = [0]
        for key in range(len(memo)):
            arr.append(memo[len(memo) - key - 1] + arr[len(arr) - 1])
        
        # print(arr)
        print(int(line[len(line) - 1]), arr[len(arr) - 1])
        ans += (int(line[len(line) - 1]) + arr[len(arr) - 1])
    print(ans) 
                

def main():
    f = open(INPUT_FILE, "r")
    input = f.readlines()
    readSequences(input)

if __name__ == "__main__":
    main()