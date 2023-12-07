INPUT_FILE = "Inputs/Day7_Input.txt"
#250104441 too high
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
jokerCards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
HAND_SCORES = {"FiveofKind" : 6, "FourofKind" : 5, "FullHouse" : 4,
                "ThreeofKind" : 3, "TwoPair" : 2, "OnePair" : 1, "HighCard" : 0}

def bubbleSort(hands):
    for i in range(len(hands)):
        swapped = False
        for j in range(0 , len(hands) - i - 1):
            x = hands[i][0]
            y = hands[i + j + 1][0]
            for c in range(len(x)):
                if cards.index(x[c]) < cards.index(y[c]):
                    tmp = hands[i]
                    hands[i] = hands[i + j + 1]
                    hands[i + j + 1] = tmp
                    swapped = True
                    break
                elif cards.index(x[c]) > cards.index(y[c]):
                    break
                
    return hands
            
def score(hand):
    cardValues = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'T':0, 'J':0, 'Q':0, 'K':0, 'A':0}
    del_keys = []
    for v in hand:
        cardValues[v] += 1

    for card, count in cardValues.items():
        if count == 0:
            del_keys.append(card)

    # keymax = max(cardValues, key= lambda x: cardValues[x])
    # # print(keymax)
    # if keymax != 'J':
    #     print(keymax, cardValues[keymax], "J", cardValues['J'])
    #     cardValues[keymax] += cardValues['J']
    #     print(cardValues[keymax])

    for i in del_keys:
        cardValues.pop(i)
    
    # if 5 in cardValues.values():
    #     return HAND_SCORES['FiveofKind']
    # if 4 in cardValues.values():
    #     return HAND_SCORES['FourofKind']
    # if 3 in cardValues.values() and 2 in cardValues.values():
    #     return HAND_SCORES['FullHouse']
    # if 3 in cardValues.values() and 2 not in cardValues.values():
    #     return HAND_SCORES['ThreeofKind']
    # if 2 in cardValues.values():
    #     if 'J' not in cardValues.keys():
    #         if len(cardValues) == 3:
    #             return HAND_SCORES['TwoPair']
    #         else:
    #             return HAND_SCORES['OnePair']
    #     else:
    #         if len(cardValues) == 4:
    #             return HAND_SCORES['ThreeofKind']

    if len(cardValues) == 1:
        return HAND_SCORES['FiveofKind']
    if len(cardValues) == 2:
        if 4 in cardValues.values():
            return HAND_SCORES['FourofKind']
        else:
            return HAND_SCORES['FullHouse']
    if len(cardValues) == 3:
        if 3 in cardValues.values():
            return HAND_SCORES['ThreeofKind']
        else:
            return HAND_SCORES['TwoPair']
    if len(cardValues) == 4:
        return HAND_SCORES['OnePair']
        
    return HAND_SCORES['HighCard']

def scoreAllHands(hands):
    dict = {6:[], 5:[], 4:[], 3:[], 2:[], 1:[], 0:[]}
    hands.sort(key = lambda x: x[2])
    for hand in hands:
        dict[hand[2]].append(hand)
    
    sortedList = []
    for key in dict.keys():
        sortedList.append(bubbleSort(dict[key]))

    sortedList = sum(sortedList, [])
    sortedList.reverse()
    ans = 0
    for i in range(len(sortedList)):
        ans += (int(sortedList[i][1]) * (i+1))
        print(sortedList[i], i, ans)

    print(ans)

def readHands(input):
    hands = []
    bids = []
    m = []
    for line in input:
        hands.append(line.split()[0])
        bids.append(line.split()[1])
    for hand in range(len(hands)):
        m.append((hands[hand], bids[hand], score(hands[hand])))
    scoreAllHands(m)

def main():
    f = open(INPUT_FILE, "r")
    input = f.read()
    readHands(input.strip().split("\n"))

if __name__ == "__main__":
    main()