n = int(input("Enter amount of elements: "))
a = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter a number: "))

count = 0
for i in a:
    if i == x:
        count += 1
print(count)
