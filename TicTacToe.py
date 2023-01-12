### make a list of all the posible squares for example A1, A2, A3, B1...
def gameboard():
    card = [] #
    rows = [1, 2, 3]
    columns = ["A", "B", "C"]
    for row in rows:
        for col in columns:
            card.append([row, col, "empty"]) # options: empty, cross, circle
    return card

list = []
### creates a sequnce that is later used in printboard for the state [2]
def counter():
    x = 0
    for a in range(3):
        for b in range(3):
            for c in range (3):
                list.append(c+x)
        x += 3


class printboard():
    ### print the entire board with empty, cross, or circle
    def __init__(self):
        line = 1
        print()
        print("    A     B     C")
        print()
        square = 0
        self.templine = ""
        for i in range(1,10):
            #self.templine += "  "
            if i == 2 or i == 5 or i ==8:
                self.line = 2 # second variation line / middle
                self.templine += str(line) +" "
                line += 1
            else:
                self.line = 1 # first variation line / top or bottom
                self.templine += "  "
            for j in range(3):
                if card[list[square]][2] == "empty": # empty square
                    self.templine += ("     ")
                elif card[list[square]][2] == "cross": # X square
                    self.printX(self.line)
                else:
                    self.printO(self.line) # O square
                if j == 0 or j == 1:
                    self.templine += ("|")
                square += 1
            self.templine += "\n"
            if i == 3 or i == 6: # These are the horizontal lines
                self.templine += (" -" * 10 + "\n")
        print(self.templine)
    ### print either top or bottom of the X
    def printX(self, line):
        if line == 1: #option 1 is for top or bottom of the X
            self.templine += (" X X ")
        else:         #option 2 is for middle of the X
            self.templine += ("  X  ")
    ### print either top or bottom of the O
    def printO(self, line):
        if line == 1: #option 1 is for top or bottom of the O
            self.templine += ("  O  ")
        else:         #option 2 is for middle of the O
            self.templine += (" O O ")

class checkwin:
    ### All of the winning options/combinations in tic tac toe
    def __init__(self):
        if card[0][2] == card[1][2] == card[2][2]: # horizontal top 
            if card[0][2] != "empty": # default is empty, check for unique combination 
                self.finish()
        if card[3][2] == card[4][2] == card[5][2]: # horizontal middle 
            if card[3][2] != "empty":
                self.finish()
        if card[6][2] == card[7][2] == card[8][2]: # horizontal bottom
            if card[6][2] != "empty":
                self.finish()
        if card[0][2] == card[3][2] == card[6][2]: # vertical left
            if card[0][2] != "empty":
                self.finish()
        if card[1][2] == card[4][2] == card[7][2]: # vertical middle
            if card[1][2] != "empty":
                self.finish()
        if card[2][2] == card[5][2] == card[8][2]: # vertical right
            if card[2][2] != "empty":
                self.finish()
        if card[0][2] == card[4][2] == card[8][2]: # diagonal \
            if card[0][2] != "empty":
                self.finish()
        if card[2][2] == card[4][2] == card[6][2]: # diagonal /
            if card[2][2] != "empty":
                self.finish()
    ### print out the winner
    def finish(self):
        if turns % 2 == 0: #checks who had the last turn
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
        exit() # ends the game after a win

card = gameboard()
counter()
valid = True
turns = 0
options = ["A 1", "B 1", "C 1", "A 2", "B 2", "C 2", "A 3", "B 3", "C 3"] # all valid user input
printboard()
for turns in range(9):
    while (valid):
        playerchoice1 = "empty" # player 1 input is set to empty
        playerchoice2 = "empty" # player 2 input is set to empty
        if turns % 2 == 0: # evens player 1 goes, odd player 2 goes
            playerchoice1 = input("Player 1 Enter Row and Column(X): ")
        else:
            playerchoice2 = input("Player 2 Enter Row and Column(O): ")
        if playerchoice1 in str(options):
            if card[options.index(playerchoice1)][2] == "empty":
                card[options.index(playerchoice1)][2] = "cross"
                valid = False
        if playerchoice2 in str(options):
            if card[options.index(playerchoice2)][2] == "empty":
                card[options.index(playerchoice2)][2] = "circle"
                valid = False
        if valid == True:
            print("invalid input please enter again (A 1)")
    valid = True
    printboard()
    checkwin()
