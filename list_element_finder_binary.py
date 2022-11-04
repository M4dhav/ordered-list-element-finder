a = int(input("How many elements do you want the list to have?\n"))
l1 = []
for i in range(a):
    l1.append(int(input("Enter a number: ")))
l1.sort()
print("\nYour List:",l1)
b = int(input("\nEnter the number you want to check for in the list: "))
def chck(x, y):
    z = x[int(len(x)/2)]
    c = int(len(x)/2)
    if len(x) <= 2:
        if y in x:
            return True
        else:
            return False
    elif y < z:
        x = x[:c +1]
    elif y > z:
        x = x[c+1:]
    elif y == z:
        return True
    d = x
    e = y
    return chck(d, e)
print("\n{}".format(chck(l1, b)))