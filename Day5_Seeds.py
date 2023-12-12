import re

INPUT_FILE = "Inputs/Day5_Input.txt"

def part1(input):
    segments = input.split("\n\n")
    seeds = re.findall(r'\d+', segments[0])

    min_location = float('inf')
    for x in map(int, seeds):
        
        for s in segments[1:]:
            for conversion in re.findall(r'(\d+) (\d+) (\d+)', s) :
                dest, start, delta = map(int, conversion)
                if x in range(start, start+delta):
                    x += dest - start
                    break
        min_location = min(x, min_location)

    return min_location

def main():
    f = open(INPUT_FILE, "r")
    input = f.read()
    print("Part1:", part1(input))

    f.close()

if __name__ == "__main__":
    main()