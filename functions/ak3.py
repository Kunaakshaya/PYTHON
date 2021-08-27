#Functions
# Greetings
def greetings():
    print("Hello!🙋🏻‍♀️")
    print("Good Morning!😊")
greetings()

#get price and give discount
def discount(x):
    d=p/10
    return(x-d)
p=int(input("Enter the price: "))
if p>500:
    print("price of the item is greater than 100🤑.10% discount will be given💰")
    print("Price=",discount(p))
else:
    print(""Price="p)

#simple calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")  
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Invalid input")

#Nested function
def name_1():
    print("Hi!")
def name_2():
    print("Hello")
name_1()
name_2()


