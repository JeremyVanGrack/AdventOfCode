INPUT_FILE = "Inputs/Day7_Input.txt"

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
HAND_SCORES = {"FiveofKind" : 6, "FourofKind" : 5, "FullHouse" : 4,
                "ThreeofKind" : 3, "TwoPair" : 2, "OnePair" : 1, "HighCard" : 0}

def score(hand):
    cardValues = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'T':0, 'J':0, 'Q':0, 'K':0, 'A':0}
    del_keys = []
    for v in hand:
        cardValues[v] += 1

    for card, count in cardValues.items():
        if count == 0:
            del_keys.append(card)
            
    for i in del_keys:
        cardValues.pop(i)
    
    if len(set(hand)) == 1:
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
    
    for key in dict.keys():
        for item in range(len(dict[key])):
            
            print(dict[5])

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