#playerchoice1 = input("Enter Row and Column(A 1): ")


def gameboard():
    card = []
    rows = [1, 2, 3]
    columns = ["A", "B", "C"]
    for row in rows:
        for col in columns:
            card.append([row, col, 1]) # 1 means empty # 2 means X # 3 means O
    return card

#### Example Board
#def printboard():
#    print("     |  O  | X X ")
#    print("     | O O |  X  ")
#    print("     |  O  | X X ")
#    horizontal()
#    #print(playerchoice1)
#    print("     |     |     ")
#    print("     |     |     ")
#    print("     |     |     ")
#    horizontal()
#    print(" X X |  O  |     ")
#    print("  X  | O O |     ")
#    print(" X X |  O  |     ")

square = 0

card = gameboard()
print(card)
class printboard():
    def __init__(self):
        self.templine = ""
        for i in range(1,10):
            self.templine += "  "
            if i == 2 or i == 5 or i ==8:
                self.line = 2 # second variation line / middle
            else:
                self.line = 1 # first variation line / top or bottom
            for j in range(3):
                global square
                if card[j][2] == 1: # 1 means empty
                    self.templine += ("     ")
                elif card[j][2] == 2: # 2 means X
                    self.printX(self.line)
                else:
                    self.printO(self.line) # 3 means O
                if j == 0 or j == 1:
                    self.templine += ("|")
                print(square, j)
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
    #def horizontal(self):
        #self.horizontal += (" -" * 10)

#print(card[1][2])
card[1][2] = 2
#print(card[1][2])
printboard()