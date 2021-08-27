#Print integers 1 to N, but print “Fizz” if an integer is divisible by 3,
 “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5

number=int(input("Enter the Number: "))
for i in range(1,number+1):
    if ((i%3==0)and(i%5==0)):
        print("FizzBuzz")
        continue
    elif i%3==0:
        print("Fizz")
        continue
    elif i%3==0:
        print("Buzz")
        continue
    else:
        print(i)
