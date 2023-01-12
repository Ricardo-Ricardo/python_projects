def gameboard():
    card = []
    rows = [1, 2, 3]
    columns = ["A", "B", "C"]
    for row in rows:
        for col in columns:
            card.append([row, col, "empty"]) # options: empty, cross, circle
    return card

list = []
def counter():
    x = 0
    for a in range(3):
        for b in range(3):
            for c in range (3):
                list.append(c+x)
        x += 3


class printboard():
    def __init__(self):
        square = 0
        self.templine = ""
        for i in range(1,10):
            self.templine += "  "
            if i == 2 or i == 5 or i ==8:
                self.line = 2 # second variation line / middle
            else:
                self.line = 1 # first variation line / top or bottom
            for j in range(3):
                if card[list[square]][2] == "empty": # 1 means empty
                    self.templine += ("     ")
                elif card[list[square]][2] == "cross": # 2 means X
                    self.printX(self.line)
                else:
                    self.printO(self.line) # 3 means O
                if j == 0 or j == 1:
                    self.templine += ("|")
                square += 1
            self.templine += "\n"
            if i == 3 or i == 6: # These are the horizontal lines
                self.templine += (" -" * 10 + "\n")
        print(self.templine)
        #horizontal()
    def printX(self, line):
        if line == 1: #option 1 is for top or bottom of the X
            self.templine += (" X X ")
        else:         #option 2 is for middle of the X
            self.templine += ("  X  ")
    def printO(self, line):
        if line == 1: #option 1 is for top or bottom of the O
            self.templine += ("  O  ")
        else:         #option 2 is for middle of the O
            self.templine += (" O O ")

### All of the winning options in tic tac toe
class checkwin():
    def __init__(self):
        gameover = True
        if card[0][2] == card[1][2] == card[2][2]:
            if card[0][2] != "empty":
                print("1")
        if card[3][2] == card[4][2] == card[5][2]:
            if card[3][2] != "empty":
                print("2")
        if card[6][2] == card[7][2] == card[8][2]:
            if card[6][2] != "empty":
                print("3")
        if card[0][2] == card[3][2] == card[6][2]:
            if card[0][2] != "empty":
                print("4")
        if card[1][2] == card[4][2] == card[7][2]:
            if card[1][2] != "empty":
                print("5")
        if card[2][2] == card[5][2] == card[8][2]:
            if card[2][2] != "empty":
                print("6")
        if card[0][2] == card[4][2] == card[8][2]:
            if card[0][2] != "empty":
                print("7")
                exit()
        if card[2][2] == card[4][2] == card[6][2]:
            if card[2][2] != "empty":
                print("Player: " + "wins!")

#playerchoice1 = input("Enter Row and Column(A 1): ")
card = gameboard()
counter()
valid = True
options = ["A 1", "B 1", "C 1", "A 2", "B 2", "C 2", "A 3", "B 3", "C 3"]
for turns in range(9):
    while (valid):
        playerchoice1 = input("Enter Row and Column(A 1): ")
        if playerchoice1 in str(options):
            if card[options.index(playerchoice1)][2] == "empty":
                card[options.index(playerchoice1)][2] = "cross"
                valid = False
        else:
            print("error please enter letter and number(A 1)")
    valid = True
    printboard()
    checkwin()

#Output - 1
print()
#card[int(playerchoice1)][2] = "cross"
#card[0][2] = "cross"
#card[1][2] = "circle"
#card[2][2] = "cross"
#card[5][2] = "cross"
#print(card[1][2])
#printboard()
#checkwin()
#print(card)
