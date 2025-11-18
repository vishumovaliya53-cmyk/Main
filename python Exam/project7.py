
import uuid
import random
import math
from datetime import datetime


# ------------------ STOPWATCH ------------------
def stopwatch():
    input("Press Enter to START the stopwatch...")
    start = datetime.now()

    input("Press Enter to STOP the stopwatch...")
    end = datetime.now()

    elapsed = (end - start).total_seconds()
    print(f"\nElapsed Time: {round(elapsed, 2)} seconds\n")


# ------------------ JOURNAL MANAGER ------------------

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


# ------------------ RANDOM DATA GENERATOR ------------------
def random_number():
    print("Random Number:", random.randint(1, 100))

def random_list():
    fruits = ["apple", "banana", "kiwi", "mango", "orange"]
    print("Random List:", random.sample(fruits, 3))

def generate_otp():
    otp = "".join(str(random.randint(0, 9)) for _ in range(6))
    print("Generated OTP:", otp)

def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    pool = letters + letters.upper() + numbers + symbols
    password = "".join(random.choice(pool) for _ in range(10))

    print("Generated Password:", password)


# ------------------ MODULE EXPLORER ------------------
def explore_module(name):
    try:
        module = __import__(name)
        attributes = [a for a in dir(module) if not a.startswith("_")]

        print(f"\nAttributes in module '{name}':")
        print(attributes)
        print()
    except ModuleNotFoundError:
        print("Module not found.\n")


# ------------------ MAIN PROGRAM ------------------
journal = filedata("main.txt")

print("\n==============================")
print("    Multi-Utility Toolkit")
print("==============================")

while True:
    print("\nMain Menu:")
    print("1. Date & Time Tools")
    print("2. Math Tools")
    print("3. Random Data Tools")
    print("4. UUID Generator")
    print("5. Journal Manager")
    print("6. Explore Modules")
    print("7. Exit")

    choice = input("Choose an option: ")

    # -------------------- DATETIME --------------------
    if choice == "1":
        while True:
            print("\nDate & Time Menu:")
            print("1. Show Current Date & Time")
            print("2. Date Difference")
            print("3. Format Current Date")
            print("4. Stopwatch")
            print("5. Back")

            ch = input("Enter choice: ")

            if ch == "1":
                now = datetime.now()
                print("\nCurrent Datetime:", now.strftime("%d-%m-%Y %H:%M:%S"))

            elif ch == "2":
                d1 = input("Enter first date (YYYY-MM-DD): ")
                d2 = input("Enter second date (YYYY-MM-DD): ")

                dt1 = datetime.strptime(d1, "%Y-%m-%d")
                dt2 = datetime.strptime(d2, "%Y-%m-%d")

                print("\nDifference:", abs((dt2 - dt1).days), "days")

            elif ch == "3":
                now = datetime.now()
                print("Formatted Date:", now.strftime("%A, %d %B %Y"))

            elif ch == "4":
                stopwatch()

            elif ch == "5":
                break

            else:
                print("Invalid choice!")

    # -------------------- MATH TOOLS --------------------
    elif choice == "2":
        print("\nMath Tools Menu:")
        print("Square Root:", math.sqrt(25))
        print("Power Example:", math.pow(2, 5))

    # ---------------- RANDOM TOOLS --------------------
    elif choice == "3":
        while True:
            print("\nRandom Data Menu:")
            print("1. Random Number")
            print("2. Random List")
            print("3. Random OTP")
            print("4. Random Password")
            print("5. Back")

            ch = input("Enter choice: ")

            if ch == "1":
                random_number()
            elif ch == "2":
                random_list()
            elif ch == "3":
                generate_otp()
            elif ch == "4":
                generate_password()
            elif ch == "5":
                break
            else:
                print("Invalid choice!")

    # -------------------- UUID --------------------
    elif choice == "4":
        print("\nGenerated UUID:", uuid.uuid4())

    # -------------------- JOURNAL --------------------
    elif choice == "5":
         print("\n1. Add new entry")
         print("2. View entries")
         print("3. Search entry")
         print("4. Delete entries")
         print("5. Exit")
         
         try:
          ch = int(input("\nEnter your choice: "))
         except ValueError:
           print("\nPlease enter a valid number.")
           continue
       
         if ch == 1:
             entry = input("\nEnter Your Journal Entry: ")
             jm.Add_Entry(entry)
    
         elif ch == 2:
              jm.View_Entry()
    
         elif ch == 3:
            print("\nShow Matching Entries:\n")
            jm.Search_Entry()
    
         elif ch == 4:
           jm.Delete_Entry()
   
         elif ch == 5:
          print("\nThank you for Using Personal Journal Manager. Goodbye!!\n")
          break
    
         else:
          print("\nInvalid Option. Please select a valid Option!")

    # -------------------- MODULE EXPLORER --------------------
         
    elif choice == "6":
     module_name = input("Enter module name to explore: ")
     explore_module(module_name) 
        
    # -------------------- EXIT --------------------
    elif choice == "7":
        print("\nExiting Multi-Utility Toolkit. Goodbye!\n")
        break


        