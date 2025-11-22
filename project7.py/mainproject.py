import uuid

from datetime_module import *
from math_module import *
from random_module import *
from Journal import FileData
from explore_module import explore_module


def main():
    # Create a journal file object for saving entries
    journal = FileData("main.txt")

    # Heading UI
    print("\n==============================")
    print("    Multi-Utility Toolkit")
    print("==============================")

    # Main loop – program continues until user chooses Exit
    while True:
        print("\nMain Menu:")
        print("choose an option:")
        print("1. Datetime and Time operations")
        print("2. Mathematical operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Indentifiers")
        print("5. File operations (custom Modules)")
        print("6. Explore Module Attribute")
        print("7. Exit")
        print("\n================================\n")

        # User choice input
        choice = input("Choose an option: ")

        # ---------------- DATE & TIME TOOLS ----------------
        if choice == "1":
            print("\nDatetime and Time operations\n")
            print("1. Display current Date and Time")
            print("2. Calcuate difference between Two Date/Time")
            print("3. Formate date into custom formate")
            print("4. Stopwatch")
            print("5. Back to Main Menu\n")

            ch = input("\nEnter choice: ")

            # Date & Time operations
            if ch == "1": 
                show_current_datetime()
            elif ch == "2": 
                date_difference()
            elif ch == "3": 
                formatted_date()
            elif ch == "4": 
                stopwatch()

        # ---------------- MATH TOOLS ----------------
        elif choice == "2":
            print("\nMathematical operations\n")
            print("1. Calculate Factorial")
            print("2. Solve Compound Intrest")
            print("3. Back to Main Menu\n ")

            ch = input("Enter choice: ")

            # Math operations
            if ch == "1": 
                factorial_value()
            elif ch == "2": 
                compound_interest()
            elif ch == "3": 
                continue
      

        # ---------------- RANDOM TOOLS ----------------
        elif choice == "3":
            print("\nRandom Data Generation\n")
            print("1. Generate random number")
            print("2. Generate random list")
            print("3. Creat random OTP")
            print("4. Generate random password")
            print("5. Back to Main Menu\n")
            
            ch = input("Enter choice: ")

            # Random operations
            if ch == "1": 
                random_number()
            elif ch == "2": 
                random_list()
            elif ch == "3": 
                generate_otp()
            elif ch == "4": 
                generate_password()
            elif ch == "5": 
                continue

        # ---------------- UUID GENERATOR ----------------
        elif choice == "4":
            # Generate new UUID
            print("\nGenerated UUID:", uuid.uuid4())


        # ---------------- JOURNAL MANAGER ----------------
        elif choice == "5":
            
            print("\nJournal Manager\n")
            print("1. Add Entry")   
            print("2. View Entries")
            print("3. Search Entry")
            print("4. Delete All Entries")
            print("5. Back to Main Menu\n")
            
            ch = input("Enter your Choice: ")
            
            # Journal operations
            if ch == "1":
                entry = input("Write your entry: ")
                journal.add_entry(entry)
            elif ch == "2": 
                journal.view_entries()
            elif ch == "3": 
                journal.search_entry()
            elif ch == "4": 
                journal.delete_entries()
                

        # ---------------- MODULE EXPLORER ----------------
        elif choice == "6":
            # Explore any module by name
            name = input("Enter module name: ")
            explore_module(name)
            

        # ---------------- EXIT PROGRAM ----------------
        elif choice == "7":
            print("\nExiting Multi-Utility Toolkit. Goodbye!\n")
            break


# Run the program
if __name__ == "__main__":
    main()
