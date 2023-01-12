list = []
def counter():
    x = 0
    for i in range(3):
        for j in range(3):
            for k in range (3):
                list.append(k+x)
        x += 3

counter()

