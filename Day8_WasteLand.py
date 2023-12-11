import re
INPUT_FILE = "Inputs/Day8_Input.txt"
myDict = {}


def partOne(directions, moves):
    for i in moves:
        m = re.split(r'[\W]+', i)
        myDict[m[0]] = (m[1], m[2])

    loc = "AAA"
    step = 0
    while True:
        for c in directions:
            step += 1
            node = myDict.get(loc)

            if c == "L":
                loc = node[0]
            else:
                loc = node[1]

            if loc == "ZZZ":
                break
        # allows us to process every char in directions until ZZZ is found
        # by else'ing the for loop we essentially say "have I found ZZZ after looping
        # the entire list of directions? if not loop them again, otherwise breakz"
        else:
            continue
        break

    return step

def main():
    f = open(INPUT_FILE, "r")
    input = f.read()
    directions = input.split()[0]
    moves = input.split("\n")[2:]
    print(partOne(directions, moves))
    
    
    f.close()

if __name__ == "__main__":
    main()