num1 = 42 # variable declaration, initialize an integer

num2 = 2.3 # variable declaration, initialize a float

boolean = True # variable declaration, initialize a boolean

string = 'Hello World' # variable declaration, initialize a string

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list declaration, initialize list with strings

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary declaration, initialize the dictionary with key and value of either string, int, or boolean 

fruit = ('blueberry', 'strawberry', 'banana') # tuples declaration, initialize with strings

print(type(fruit)) # log the Data Types of fruit to the terminal

print(pizza_toppings[1]) # log the second element in pizza_toppings list to the terminal

pizza_toppings.append('Mushrooms') # adding the value "Mushrooms" to the end of the pizza_toppings list

print(person['name']) # access the name value in the person dictionary and then log it to terminal

person['name'] = 'George' # change the name value to George in the person dictionary

person['eye_color'] = 'blue' # change the eye_color value to blue in the person dictionary

print(fruit[2]) # log the second element in the fruit list

# conditional with a if and else
""" 
    If num1 is greater than 1 , log "It's greater".
    If not then log "It's lower".
"""
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# conditional with a if, else if, and an else
""" 
    If do a length check on the string to see if it is smaller than 5.
    Else if do another length check on the string to see if it is greater than 15.
    Else log that it is between 5 - 15
"""
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loops
"""
    start at 0, end at 4, increment by 1, print the value of x every sequence
"""
for x in range(5):
    print(x)
"""
    start at 2, end at 4, increment by 1, print the value of x every sequence
"""    
for x in range(2,5):
    print(x)
"""
    start at 2, end at 9, increment by 3, print the value of x every sequence
"""
for x in range(2,10,3):
    print(x)
    
# while loop
"""
    start at 0, end at 4, increment by 1, print the value of x every sequence    
"""
x = 0
while(x < 5):
    print(x)
    x += 1


pizza_toppings.pop() # Remove the last element in the list
pizza_toppings.pop(1) # Remove the element in the index 1 slot

print(person) # log the person dictionary
person.pop('eye_color') # Remove the key "eye_color" and the value that goes with it
print(person) # log the updated person dictionary 

# for loop with conditional if statements
"""
    loop through the pizza_toppings list
    If the topping is Pepperoni, continue onto the next topping.
    If the topping is not Pepperoni, log "After 1st if statement".
    If the topping is Olives, then quit outside the for loop.
    Increment to the next topping for the loop if there is.
"""
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

# function with no parameter and a for loop
"""
    for loop start at 0, end at 9, print hello 10 times, increment by 1
"""
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
# call the function with no argument
print_hello_ten_times()

# function with 1 parameter and a for loop
"""
    for loop start at 0, end at x - 1, increment by 1, print hello x times
"""
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

# call the function with an argument
print_hello_x_times(4)

# function with 1 parameter, with a default argument of 10
"""
    for loop start at 0, end at 9 if no argument pass and x-1 if argument is pass, increment by 1, print hello x times
"""
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # call the function with no argument
print_hello_x_or_ten_times(4) # call the function with an argument


"""
Bonus section
"""

print(num3) #NameError
num3 = 72 # variable declaration, initialize Integer
fruit[0] = 'cranberry' # TypeError
print(person['favorite_team']) # KeyError 
print(pizza_toppings[7]) #IndentationError
print(boolean) # log the boolean variable
fruit.append('raspberry') # AttributeError
fruit.pop(1) # AttributeError