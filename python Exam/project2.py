print()
print("Welcome to the Pattern Generator and Number Analyzer!")
sum = 0
print()

while True: 
    print("Select an option: ")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        choice1 = int(input("Enter the number of rows for the pattern: "))
        print()
        print("Pattern:")
        for i in range(1, choice1 + 1):
            print("*" * i)
        print()

    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        for i in range(start, end + 1):
            if i % 2 == 0:
                print("Number", i, "is Even")
            else:
                print("Number", i, "is Odd")
            sum = sum + i
        print("Sum of all numbers from", start, "to", end, "is:", sum)
        print()

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        print()
        break

    else:
        print()
        print("Your choice is not valid.")