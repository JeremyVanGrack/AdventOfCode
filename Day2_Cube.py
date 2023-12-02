import re

INPUT_FILE = "Inputs/Day2_Input.txt"
R_MAX = 12
G_MAX = 13
B_MAX = 14

class Game:
    def __init__(self, id=0, red=0, green=0, blue=0):
        self.id = id
        self.red = red
        self.green = green
        self.blue = blue

#parse games
def parseGames(list):
    for game in list:
        r, g, b = 0, 0, 0
        game = re.split(': |; |,', game)
        gameID = game[0].split()
        # remove "Game X: from front"
        game = game[1:]

        # grab max RGB values
        for entry in game:
            if "red" in entry:
                r = max(r, int(entry.split()[0]))
            elif "green" in entry:
                g = max(g, int(entry.split()[0]))
            else:
                b = max(b, int(entry.split()[0]))
        
        # put Game into list
        maxGame = Game(gameID[1], r, g, b)

        try:
            gameList.append(maxGame)
        except:
            gameList = [maxGame]

    return gameList

#only count games possible based off global RGB value
def countPossibleGames(list):
    ans = 0
    for game in list:
        if game.red <= R_MAX and game.green <= G_MAX and game.blue <= B_MAX:
            ans += int(game.id)
        else:
            print("Invalid Game:", game.id)
    
    print("Sum of Valid Games:", ans)
    return ans  

#counts minimum number of each cube needed to make each 
#game possible
def countMinPossibility(list):
    ans = 0
    for game in list:
        power = game.red * game.green * game.blue
        ans += power

    print("Sum of Powers of All Games:", ans)

def main():
    f = open(INPUT_FILE, 'r')
    games = f.readlines()
    list = parseGames(games)
    count = countPossibleGames(list)
    min_count = countMinPossibility(list)

if __name__ == "__main__":
    main()
