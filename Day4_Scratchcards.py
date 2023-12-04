INPUT_FILE = "Inputs/Day4_Input.txt"

def cards(input):
    for line in input:
        M = [x.split() for x in ( (line.split(": ")[1]).split(" | "))]
        try:
            arr.append(M)
        except:
            arr = [M]
    
    count = 0
    for i in arr:
        for k in i[1]:
            if k in i[0]:
                if count == 0:
                    count += 1
                else:
                    count *= 2
    print(count)

def main():
    f = open(INPUT_FILE, "r")
    input = f.readlines()
    cards(input)

if __name__ == "__main__":
    main()