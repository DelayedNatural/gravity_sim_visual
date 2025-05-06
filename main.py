import time

d = int(input("Δώστε την απόσταση του αντικειμένου από το έδαφος (Maximum 50): ")) #initial position of object
w = int(input("Δώστε το βάρος: "))
x = d #position of object
i = d
dtemp = d
while i >= 0:
    while dtemp >= 0:
        if x == d:
            print("☐")
        print("")
        dtemp -= 1
    for i2 in range(d):
        print("")
    i -= 1
    time.sleep(1)