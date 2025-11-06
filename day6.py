print("Welcome to the Interactive person data collector \n")

name = str(input("Enter your name : "))
age = int(input("Enter your age : "))
height = int(input("Enter your height : "))
FavoriteNumber = int(input("Enter your favorite number : \n"))

print("Thank you! Here is the information we collected: \n")

print("Name :",name,("Type :",type(name),"memory address :", id(name)))
print("Age :",age,("Type :",type(age),"memory address :", id(age)))
print("Height :",height,("Type :",type(height),"memory address :", id(height)))
print("Favorite Number :",FavoriteNumber,("Type :",type(FavoriteNumber),"memory address :", id(FavoriteNumber)))

print("\n")

print("your birth year is Approximately: \n",2025 - age,("based on age of",age))

print("Thank you for using the personal Data Collector. Goodbye!")