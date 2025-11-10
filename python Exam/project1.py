print("Welcome to the Interactive Personal Data Collector")

print()

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favoritenumber = int(input("Please enter your favorite number: "))
                  
print()

print("Thank you! Here is the information we collected: ")

print()

print("Name :",name,("Type :",type(name),"memory address :", id(name)))
print("Age :",age,("Type :",type(age),"memory address :", id(age)))
print("Height :",height,("Type :",type(height),"memory address :", id(height)))
print("Favorite Number :",favoritenumber,("Type :",type(favoritenumber),"memory address :", id(favoritenumber)))

print()

print("your birth year is Approximately:",2025 - age,("based on age of",age))

print()

print("Thank you for using the personal Data Collector. Goodbye!")