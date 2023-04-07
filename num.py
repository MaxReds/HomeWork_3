n = int(input("Enter amount of elements:"))
a = list(map(int, input("Enter elements: ").split()))
x = int(input("Eneter a number: "))
 
dif = abs(a[0] - x)
num = a[0]
 
for i in a:
    if abs(i - x) < dif:
        dif = abs(i - x)
        num = i
 
print(num)



