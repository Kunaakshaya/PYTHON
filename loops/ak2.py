#LOOPS
#while loop
i=1
while i<=5:
    print("computer ",end="")
    j=1
    while j<=1:
        print("science ",end="")
        j=j+1
    i=i+1
    print()
#for loop
digits=int(input("Enter a num: "))
for i in range(1,digits):
    if(i%2==0):
        print("it's an even num")
    else:
        print("it's not an even num")
print("num is not found")
