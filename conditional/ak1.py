#Conditional statements.
#checking the Cost.
Products="Laptops","Phones","Books","Earphones","etc..."
print(Products)

# if Statement
Items=input("Enter Name of the product:")
if(Items=="Laptops"):
    print("Laptops are available")
    print("Dell-","HP-","Samsung-etc...")
    print("Cost of the laptops start from 30k to 10 lakhs")
          
# if-else statement
Items=input("Enter Name of the product:")
# checking if the iteam is available or not...
if(Items=="Laptops"):
    print("Laptops are available")  #if condition true..
else:
    print("Item is not available")  #if condition false..
    

#if-elif-else statement
Items=input("Enter Name of the product:")
#Cost of the Items Range...
if(Items=="Laptops"):
    print("Laptops are available")
    print("Dell-","HP-","Samsung-etc...")
    print("Cost of the laptops start from 30k to 10 lakhs")
elif(Items=="Phones"):
    print("Phones are available")
    print("samsung-","iphone-","apple-etc...")
    print("Cost of the phones start from 5k to 1 lakhs")
elif(Items=="Books"):
    print("All types of books are available")
else:
    print("Required items are not available")

#Nested if statement.
Items=input("Enter Name of the product:")
system=input("Enter system name:")
if(Items=="Phones"):
    if(system=="samsung"):
        print("Cost of the Required product start from 10,500 to 45,000")
    elif(system=="apple"):
        print("Cost of the Required product start from 15,500 to 1 lakh")
    elif(system=="vivo"):
        print("Cost of the Required product start from 20,500 to 65,000")
    else:
        print("System is not available")
else:
    print("Item is not available")

