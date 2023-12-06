INPUT_FILE = "Inputs/Day4_Input.txt"

def dynamicallyProgram(arr):
    # make look up table
    c = [1]*len(arr)

    # parse and loop cards
    for cardId,line in enumerate(arr):
        cards = line.strip().split(": ")[1].split(" | ")
        
        # set of winning numbers
        win = set(cards[0].split(" "))
        if '' in win:
            win.remove('')

        # set of numbers that may match winning numbers
        mine = set(cards[1].split(" "))

        # get matching values of card
        points = len(win.intersection(mine))

        # assign point value to next cardId based off current cardId in lookup table
        for j in range(points):
            c[j+cardId+1] = c[j+cardId+1] + c[cardId]

    print("Part 2:", sum(c))

def cards(input):
    for line in input:
        id = (line.split(": ")[0]).split()[1]
        # print(id)
        M = [x.split() for x in ( (line.split(": ")[1]).split(" | "))]
        try:
            arr.append(M)
        except:
            arr = [M]
    
    sum = 0
    for i in arr:
        count = 0
        for k in i[1]:
            if k in i[0]:
                if count == 0:
                    count += 1
                else:
                    count *= 2
        sum += count

    print("Part 1:", sum)

def main():
    f = open(INPUT_FILE, "r")
    input = f.readlines()
    cards(input)
    dynamicallyProgram(input)

if __name__ == "__main__":
    main()