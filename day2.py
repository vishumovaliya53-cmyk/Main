# Three type of control structures

"""
1. Sequential control 
2. Selection control
3. Looping control
"""

# 1.Sequential control structure --> statements are executed one after one

print("Hello")
print("Welcome to python")
print("Enjoy coding!")

#1.Selection control structure --> execute different code blocks based on conditions

'''
1. if statment
'''

num = int(input("Enter a number: "))

if num> 0:
    print("This number is positive")



age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for vote")
    
    
    

num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:  
    print(f"{num} is a positive even number.")
    

'''
2. if else statements
'''

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.") 
else:
    print(f"{number} is an odd number.")



age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



num = int(input("Enter a number: "))

if num >= 0:
    print("Positive Number")
else:
    print("Negative Number")
 
 
    
text = input("Enter some text: ")

if text:
    print("You entered:", text)
else:
    print("You entered an empty string!")
    


'''
if else elif
'''

marks = int(input("Enter your marks: "))
 
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")
    
 
    
day = int(input("Enter a number (1-7) for day of the week: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")
    


temp = int(input("Enter a number(0 -32)for temputer: "))

if temp < 0:
    print("It's freezing!")
elif temp >= 0 and temp < 10:
    print("It's cold!")
elif temp >= 10 and temp < 20:
    print("It's cool!")
elif temp >= 20 and temp < 30:
    print("It's warm!")
else:
    print("It's hot!")
    


age = int(input("Enter your age: "))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 35:
    print("Adult")
elif age <= 60:
    print("Middle-aged")
else:
    print("Senior Citizen")