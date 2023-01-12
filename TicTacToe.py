playerchoice1 = input("Enter Row and Column(A 1): ")


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

def horizontal():
    horizontal = print(" -" * 10)
    return horizontal

card = gameboard()
print(card)
class printboard():
    def __init__(self):
        self.templine = ""
        for i in range(3):
            if card[i][2] == 1:
                #self.templine += ("     ")
                self.printX(1)
            elif card[i][2] == 2:
                self.printX()
            else:
                self.printO()
        print(self.templine)
        horizontal()
    def printX(self, line):
        if line == 1:
            #print("yes")
            self.templine += (" X X ")
        else:
            #self.template += ("  X  ")
            print("no")
    def printO(self, line):
        if line == 1:
            #self.template += ("  O  ")
            print("no")
        else:
            #self.template += (" O O ")
            print("no")
printboard()