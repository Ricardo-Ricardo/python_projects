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



card = gameboard()
print(card)
class printboard():
    def __init__(self):
        self.templine = ""
        for i in range(1,10):
            if i == 2 or i == 5 or i ==8:
                self.line = 2
            else:
                self.line = 1
            for j in range(3):
                if card[j][2] == 1: # 1 means empty
                    #self.templine += ("     ")
                    self.printX(1)
                elif card[j][2] == 2: # 2 means X
                    self.printX()
                else:
                    self.printO() # 3 means O
            self.templine += "\n"
            if i == 3 or i == 6:
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
printboard()