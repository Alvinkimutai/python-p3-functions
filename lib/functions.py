#!/usr/bin/env python3

def greet_programmer():
    # pass
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    # pass
    print(f"Hello, {name}!")
greet('Alvin')

def greet_with_default(name="programmer"):
    # pass
    print(f"Hello, {name}!")
greet_with_default()

def add(num1, num2):
    # pass
   result= num1+num2
   print(result)
   return result
add(45, 55)

def halve(number):
    #  pass
    if isinstance (number, int) or isinstance(number, float):
     return number/2
    
theHalf= halve(5)
print(theHalf)
