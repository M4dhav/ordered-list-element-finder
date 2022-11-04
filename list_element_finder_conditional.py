a = int(input("How many elements do you want the list to have?\n"))
l1 = []
for i in range(a):
    l1.append(int(input("Enter a number: ")))
l1.sort()
print("Your List:",l1)
b = int(input("Enter the number you want to check for in the list: "))
if b in l1:
    print(True)
else:
    print(False)