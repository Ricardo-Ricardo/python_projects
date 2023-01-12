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

def printX(line):
    if line == 1:
        print(" X X ")
    else:
        print("  X  ")
def printO(line):
    if line == 1:
        print("  O  ")
    else:
        print(" O O ")
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
                self.templine += ("     ")
            elif card[i][2] == 2:
                printX()
            else:
                printO()
        print(self.templine)
        horizontal()

printboard()