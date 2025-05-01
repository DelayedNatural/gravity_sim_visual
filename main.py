d = int(input("Give the distance of the object from the ground in meters: ")) #initial position of object
w = int(input("Give the weight of the object: "))
x = d #position of object
dtemp = d
while x > 0:
    while dtemp > x:
        print(" ")
        dtemp -= 1
    dtemp = d
    print("☐")
    x -= 1