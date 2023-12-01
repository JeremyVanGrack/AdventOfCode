import re

INPUT_FILE = "Day1_Input.txt"

def atoi(word):
    word = word.lower()
    
    numDict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
                'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

    for num in numDict.keys():
        
        replacement = num + str(numDict[num]) + num
        word = word.replace(num, replacement)
        print(replacement)

    return word

def getFirstAndLast(list):
    ans = 0
    for word in list:
        word = atoi(word.lower())

        allNums = [i for i in word if i.isdigit()]
        if allNums:
            first = allNums[0]
            last = allNums[len(allNums) - 1]
        else:
            continue

        concat = "".join([str(first), str(last)])
        print("cat:", concat)
        ans += int(concat)
    return ans

def main():
    f = open(INPUT_FILE, 'r')
    list = f.readlines()

    print("Answer:", getFirstAndLast(list))

if __name__ == "__main__":
    main()
