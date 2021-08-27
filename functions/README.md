### Functions
* A function is a block of organized, reusable code tat is used to perform a single, related
action. 
* Functions provide better modularity for your applications and a high degree of code 
reusing.
* Functions
    * Built-in functions or predefined functions
    * User defined functions

#### user defined functions
* The functions defined by the users according to their requirements are called user defined 
function.
* The users can modify the function according to their requirement.

##### ELEMENTS OF USER DEFINED FUNCTIONS 
* Function definition:
 The definition of function contains the code that determines the 
functions behaviour.
#### SYNTAX
```python
def function_name(parameters):
    statement 1
        .
        .
    statement n
```
* Function call:
    * A function is used within a program using function call.
    * You can execute function by calling it from another function or directly from the Python 
prompt.
#### SYNTAX
```python
 function_name(parameters)
```
### Parameters and Arguments
* A function can take parameters, which are values you supply to the function so that the 
function can do something utilizing those values.
* The names of values given in the function definition is called parameters, whereas the 
values supply in the function call are called argument.

#### Return statement
* The return statement ma or may not send back any values to the main program.
* It can be done using return statement.
##### ex:
```python
def sum(x,y):
 tot=x+y
 print "Inside function total=",tot
 return tot;
total=sum(100,200)
print "Outside function total=",total
```
#### Fruitful Function
* A function that yields a return value is called fruitful function.
##### ex:
```python
def sum(x,y):
 tot=x+y 
 return tot
total=sum(100,200)
print “total=",total
```
#### Function Arguments
#### Positional Arguments
#### Keyword Arguments
#### variable length Arguments
#### Nested Functions
#### First class Functions
#### Higher Order Functions
#### Anonymous Functions
#### Function Composition