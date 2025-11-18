# import datetime
# import uuid
# import math

# class filedata:
#     def __init__ (self,filename="main.txt"):
#         self.filename=filename

#     def Add_Entry(self,entry):
#         with open(self.filename,"a") as file:
#             now = datetime.datetime.now()
#             print(now)
#             file.write(entry + "\n") 
#             print("\nEntry Added successfully !!")
            
#     def View_Entry(self):
#         try:
#             with open(self.filename,"r")as file:
#                 v=file.read()
#                 print("\n--- Journal Entries ---\n")
#                 now = datetime.datetime.now()
#                 print(now)
#                 print(v)
#         except FileNotFoundError:
#             print("\nNo Journal Entries found. Start by Adding New Entry!")
            
#     def Search_Entry(self):
#         s=input("\nEnter A Keyword for Search: ")
#         with open("main.txt","r")as file:
#             a=file.readlines ()
#         for linenum, a in enumerate(a):
#             if s in a:
#                 print(linenum , "     " , a)
#             else:
#                 print("No Entries Were Found For The Keyword !!")
                
#     def Delete_Entry(self):
#         with open (self.filename,"w") as file:
#             file.write("")
#         verify = str(input("\nYou Want To Delete This File(y/n): "))
#         if verify == "y":
#             print("\nAll journal have been deleted!!")
#         elif verify == "n":
#             print("\nDone")
#         else:
#             print("\nNo journal Entries to Delete.") 
            
# jm = filedata("main.txt")

# def date_time_operations():
#     while True:
#         print("\nDate and Time Operations:")
#         print("1. Show current date/time")
#         print("2. Calculate days between two dates")
#         print("3. Add days to current date")
#         print("4. Back to main menu")
        
#         choice = input("Enter your choice: ")

#         if choice == 1:
#             print("\nCurrent date and time:", datetime.datetime.now())

#         elif choice == 2:
#             d1 = input("Enter the first date (YYYY-MM-DD): ")
#             d2 = input("Enter the second date (YYYY-MM-DD): ")
#             d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
#             d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
#             print("Days between:", abs((d2 - d1).days))

       
#         elif choice == 4:
#             return
#         else:
#             print("Invalid input!")


# def math_operations():
#     while True:
#         print("\nMathematical Operations:")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Square Root")
#         print("6. Back to main menu")

#         choice = input("Enter your choice: ")

#         if choice in [1, 2, 3, 4]:
#             a = float(input("Enter number 1: "))
#             b = float(input("Enter number 2: "))

#             if choice == 1:
#                 print("Result =", a + b)
#             elif choice == 2:
#                 print("Result =", a - b)
#             elif choice == 3:
#                 print("Result =", a * b)
#             elif choice == 4:
#                 if b != 0:
#                     print("Result =", a / b)
#                 else:
#                     print("Cannot divide by zero!")

#             elif choice == 5:
#               n = float(input("Enter number: "))
#             print("Square root =", math.sqrt(n))

#         elif choice == "6":
#             return
#         else:
#             print("Invalid choice!")



# def string_operations():
#     while True:
#         print("\nString Operations:")
#         print("1. Count vowels")
#         print("2. Reverse string")
#         print("3. Convert to uppercase")
#         print("4. Convert to lowercase")
#         print("5. Back to main menu")

#         choice = input("Enter your choice: ")

#         if choice in ["1", "2", "3", "4"]:
#             s = input("Enter a string: ")

#             if choice == 1:
#                 vowels = "aeiouAEIOU"
#                 count = sum(1 for c in s if c in vowels)
#                 print("Total vowels:", count)

#             elif choice == 2:
#                 print("Reversed string:", s[::-1])

#             elif choice == 3:
#                 print("Uppercase:", s.upper())

#             elif choice == 4:
#                 print("Lowercase:", s.lower())

#         elif choice == 5:
#             return
#         else:
#             print("Invalid input!")



# def file_operations():
#     while True:
    
#        print("\n1. Add new entry")
#        print("2. View entries")
#        print("3. Search entry")
#        print("4. Delete entries")
#        print("5. Exit")

#        try:
#         choice = int(input("\nEnter your choice: "))
#        except ValueError:
#         print("\nPlease enter a valid number.")
#         continue

#        if choice == 1:
#         entry = input("\nEnter Your Journal Entry: ")
#         jm.Add_Entry(entry)
    
#        elif choice == 2:
#         jm.View_Entry()
    
#        elif choice == 3:
#         print("\nShow Matching Entries:\n")
#         jm.Search_Entry()
    
#        elif choice == 4:
#         jm.Delete_Entry()
   
#        elif choice == 5:
#         print("\nThank you for Using Personal Journal Manager. Goodbye!!\n")
#         break
    
#        else:
#         print("\nInvalid Option. Please select a valid Option!")
        
        
# def uuid__operations():
#                    while True:
#                        print("\nGenerate Unique Indentifiers\n") 
#                        print("1. Generate UUID")
#                        print("2. Back to Main Menu\n ")
            
#                        ch = int(input("Enter a number: "))
            
#                        if ch == 1 :
#                           Id = uuid.uuid4() 
#                        print(f"Generated UUID: {Id}") 
#                        print("\n================================\n")
                




# # ---------------------- MAIN MENU ---------------------- #


# while True:
#     print("\nWelcome to Multi-Utility Toolkit")
#     print("\nChoose an option:")
#     print("1. Date & Time Operations")
#     print("2. Mathematical Operations")
#     print("3. String Operations")
#     print("4. File Operations")
#     print("5. Display Mobile Attributes (Info)")
#     print("6. Exit")

#     ch = input("Enter your choice: ")

#     if ch == 1:
#         date_time_operations()
#     elif ch == 2:
#         math_operations()
#     elif ch == 3:
#         string_operations()
#     elif ch == 4:
#         file_operations()
#     elif ch == 5:
#         uuid__operations()
#     elif ch == 6:
#         print("Exit...")
#         break
#     else:
#         print("Invalid choice!")



from datetime import datetime
import datetime

class filedata:
    def __init__ (self,filename="main.txt"):
        self.filename=filename

    def Add_Entry(self,entry):
        with open(self.filename,"a") as file:
            now = datetime.datetime.now()
            print(now)
            file.write(entry + "\n") 
            print("\nEntry Added successfully !!")
            
    def View_Entry(self):
        try:
            with open(self.filename,"r")as file:
                v=file.read()
                print("\n--- Journal Entries ---\n")
                now = datetime.datetime.now()
                print(now)
                print(v)
        except FileNotFoundError:
            print("\nNo Journal Entries found. Start by Adding New Entry!")
            
    def Search_Entry(self):
        s=input("\nEnter A Keyword for Search: ")
        with open("main.txt","r")as file:
            a=file.readlines ()
        for linenum, a in enumerate(a):
            if s in a:
                print(linenum , "     " , a)
            else:
                print("No Entries Were Found For The Keyword !!")
                
    def Delete_Entry(self):
        with open (self.filename,"w") as file:
            file.write("")
        verify = str(input("\nYou Want To Delete This File(y/n): "))
        if verify == "y":
            print("\nAll journal have been deleted!!")
        elif verify == "n":
            print("\nDone")
        else:
            print("\nNo journal Entries to Delete.") 
            
jm=filedata("main.txt")


print("Welcome to Multi-utility Toolkit")

while True:
    print("\nChoose an option:")
    print("1. Date and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Indentifiers")
    print("5. File operations (custom Modules)")
    print("6. Explore Module Attribute")
    print("7. Exit")
    print("\n================================\n")
    choice = int(input("Enter your choice: "))

    # ---------------------------
    # 1. DATE & TIME OPERATIONS
    # ---------------------------
    if choice == 1:
        print("\nDate and Time Operations:")
        print("a. Show current date/time")
        print("b. Calculate difference between two dates")
        print("c. Convert date format (YYYY-MM-DD to DD-MM-YYYY)")

        sub = input("Enter your choice: ")

        # a. Show current date/time
        if sub == a:
            now = datetime.now()
            print("Current date and time :", now)

        # b. Date difference
        elif sub == b:
            d1 = input("Enter the first date (YYYY-MM-DD): ")
            d2 = input("Enter the second date (YYYY-MM-DD): ")

            date1 = datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.strptime(d2, "%Y-%m-%d")

            diff = date2 - date1
            print("Difference:", diff.days, "days")

        # c. Format conversion
        elif sub == c:
            c = input("Enter the date (YYYY-MM-DD): ")
            new_date = datetime.strptime(d, "%Y-%m-%d").strftime("%d-%m-%Y")
            print("Converted date:", new_date)

    # ---------------------------
    # 2. MATHEMATICAL OPERATIONS
    # ---------------------------
    elif choice == 2:
        print("\nMathematical Operations:")

        sub = int(input("Enter your choice: "))

        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))

        if sub == 1:
            print("Sum =", a + b)
        elif sub == 2:
            print("Difference =", a - b)
        elif sub == 3:
            print("Product =", a * b)
        elif sub == 4:
            if b != 0:
                print("Quotient =", a / b)
            else:
                print("Error: Cannot divide by zero!")

    # ---------------------------
    # 3. STRING OPERATIONS
    # ---------------------------
    elif choice == 3:
        print("\nString Operations:")
        print("1. Count length of string")
        print("2. Convert to uppercase")
        print("3. Convert to lowercase")
        print("4. Reverse string")

        sub = int(input("Enter your choice: "))
        s = input("Enter string: ")

        if sub == 1:
            print("Length:", len(s))
        elif sub == 2:
            print("Uppercase:", s.upper())
        elif sub == 3:
            print("Lowercase:", s.lower())
        elif sub == 4:
            print("Reversed:", s[::-1])

    # ---------------------------
    # 4. FILE OPERATIONS
    # ---------------------------
    elif choice == 4:
        while True:
    
         print("\n1. Add new entry")
         print("2. View entries")
         print("3. Search entry")
         print("4. Delete entries")
         print("5. Exit")

      try:
             sub = int(input("\nEnter your choice: "))
      except ValueError:
        print("\nPlease enter a valid number.")
        continue

    if sub == 1:
        entry = input("\nEnter Your Journal Entry: ")
        jm.Add_Entry(entry)
    
    elif sub == 2:
        jm.View_Entry()
    
    elif sub == 3:
        print("\nShow Matching Entries:\n")
        jm.Search_Entry()
    
    elif sub == 4:
        jm.Delete_Entry()
   
    elif sub == 5:
        print("\nThank you for Using Personal Journal Manager. Goodbye!!\n")
        break
    
    else:
        print("\nInvalid Option. Please select a valid Option!")

    # ---------------------------
    # 5. MATRIX OPERATIONS (2×2)
    # ---------------------------
   
     elif choice == 5:
        print("\nMatrix Operations for 2x2 Matrices:")

        print("Enter matrix A:")
        a11 = int(input("a11: "))
        a12 = int(input("a12: "))
        a21 = int(input("a21: "))
        a22 = int(input("a22: "))

        print("\nEnter matrix B:")
        b11 = int(input("b11: "))
        b12 = int(input("b12: "))
        b21 = int(input("b21: "))
        b22 = int(input("b22: "))

        print("\n1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        op = int(input("Enter your choice: "))

        if op == 1:
            print("\nResult:")
            print(a11 + b11, a12 + b12)
            print(a21 + b21, a22 + b22)

        elif op == 2:
            print("\nResult:")
            print(a11 - b11, a12 - b12)
            print(a21 - b21, a22 - b22)

        elif op == 3:
            print("\nResult:")
            print(a11*b11 + a12*b21, a11*b12 + a12*b22)
            print(a21*b11 + a22*b21, a21*b12 + a22*b22)

    # ---------------------------
    # EXIT PROGRAM
    # ---------------------------
    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")

