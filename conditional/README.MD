### conditional statements
  * Conditional statements are also called decision making statements.
  * We use those statements when we want to execute a block of code when the given condition is true or false.

#### Types of conditional statements 
* if(conditional statement)
* if-else(alternative conditional statement)
* if-elif-else(chain conditional statement)
* nested if

#### if statements
 It decides whether statements need to be executed or not.It checks for a given condition,if the condition is true, then the set of code present inside the ” if ” block will be executed otherwise not.
 **SYNTAX**
 ```python
    if(expression==true):
        #Block of code
 ```   
#### if-else statements
If a given condition is true then execute the statements present inside the “if block” and if the condition is false then execute the “else” block.
**SYNTAX**
```python
  if(expression==true):
      #Block of code
  else:
      #Block of code
```

#### if-elif-else statements
"elif" statement is used to check multiple conditions only if the given condition is false. It’s similar to an “if-else” statement and the only difference is that in “else” we will not check the condition but in “elif” we will check the condition.
**SYNTAX**
```python
   if(condition1):
        #Block of code
   elif(condition2):
       #Block of code
    else:
        #False Block of code
```

#### Nested statements
writing conditional statements inside the condition.
**SYNTAX**
```python
   if condition1:
      if condition2: 
          #statements
      else:
          #statements
   else:
       if condition3:
           #statements
       else:
           #statements
```      




