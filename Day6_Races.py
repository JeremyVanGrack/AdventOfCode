INPUT_FILE = "Inputs/Day6_Input.txt"

def compute(t, d):
    ans = 0
    for tx in range(t + 1):
        if(tx * (t - tx) >= d):
            ans += 1

    return ans

def Races(L, part_one):
    if part_one:
        T = [int(x) for x in L[0].split(":")[1].split()]
        D = [int(x) for x in L[1].split(":")[1].split()]

        times = []
        for i in range(len(T)):
            times.append(compute(T[i], D[i]))

        x = 1
        for i in times:
            x *= i
        print(x)

    else:
        T = "".join([x for x in L[0].split(":")[1].split()])
        D = "".join([x for x in L[1].split(":")[1].split()])
        time = compute(int(T), int(D))
        print(time)

def main():
    f = open(INPUT_FILE, "r")
    input = f.read()
    Races(input.strip().split("\n"), 0)

if __name__ == "__main__":
    main()