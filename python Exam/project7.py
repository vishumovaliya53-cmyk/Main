
from datetime import datetime 
now = datetime.now()    
import uuid
import random

 
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
            

print("\n================================")
print("Welcome to Multi-utility Toolkit")
print("================================\n")
while True:
    print("choose an option:")
    print("1. Datetime and Time operations")
    print("2. Mathematical operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Indentifiers")
    print("5. File operations (custom Modules)")
    print("6. Explore Module Attribute")
    print("7. Exit")
    print("\n================================\n")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        while True:
            print("\nDatetime and Time operations\n")
            print("1. Display current Date and Time")
            print("2. Calcuate difference between Two Date/Time")
            print("3. Formate date into custom formate")
            print("4. Stopwatch")
            print("5. Back to Main Menu\n")
            
            ch = int(input("Enter a number: "))
            
            if ch == 1:
                print(f"Current Date and Time: {now.strftime("%d-%m-%Y %H:%M:%S")}")
            
            elif ch == 2 :

                date1_str = input("Enter the first date (YYYY-MM-DD): ")
                date2_str = input("Enter the second date (YYYY-MM-DD): ")

                date1 = datetime.strptime(date1_str, "%Y-%m-%d")
                date2 = datetime.strptime(date2_str, "%Y-%m-%d")

                difference = date1 - date2

                print("Difference:", difference.days, "days")
                
            elif ch == 3:
                
                formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
                print("Formatted Date:", formatted_date)

                date_string = formatted_date
                converted_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
                print("Converted Datetime Object:", converted_date)
                
            elif ch == 4 :
                days = int(input("Enter number of days to add: "))
                n_date = datetime.datetime.now() + datetime.timedelta(days=days)
            print("New date:", n_date)

    elif choice == 3:
                while True:
                   print("\nRandom Data Generation\n")
                   print("1. Generate random number")
                   print("2. Generate random list")
                   print("3. Creat random OTP")
                   print("4. Generate random password")
                   print("5. Back to Main Menu\n ")
            
                   ch = int(input("Enter a number: "))
            
                   if ch == 1 :
                     print(random.randint(1,100))
                
                   elif ch == 2 :
                    items = ["BMW", "Mahindra", "TATA", "Rolls-Royce"]
                    random_list = random.sample(items, k=3)
                    print(random_list)
            
                   elif ch == 3 :
                    otp = " "
                    for i in range(6):
                     otp += str(random.randint(0, 9))
                    print("Your OTP:", otp) 
            
                   elif ch == 4 :
                    letters = "abcdefghijklmnopqrstuvwxyz"
                    numbers = "0123456789"
                    symbols = "!@#$%^&*"

                    all_chars = letters + letters.upper() + numbers + symbols

                    password = ""
                    for i in range(8):
                     password += random.choice(all_chars)

                    print("Your Password:", password)
    
    elif choice == 4:
            while True:
                   print("\nGenerate Unique Indentifiers\n") 
                   print("1. Generate UUID")
                   print("2. Back to Main Menu\n ")
            
                   ch = int(input("Enter a number: "))
            
                   if ch == 1 :
                     Id = uuid.uuid4() 
                     print(f"Generated UUID: {Id}") 
                     print("\n================================\n")
                    
    elif choice == 5:
        jm=filedata("main.txt")

    while True:

       print("\n1. Add new entry")
       print("2. View entries")
       print("3. Search entry")
       print("4. Delete entries")
       print("5. Exit")

       try:
           choice = int(input("\nEnter your choice: "))
       except ValueError:
        print("\nPlease enter a valid number.")
        continue

       if choice == 1:
           entry = input("\nEnter Your Journal Entry: ")
           jm.Add_Entry(entry)
    
       elif choice == 2:
          jm.View_Entry()
    
       elif choice == 3:
         print("\nShow Matching Entries:\n")
         jm.Search_Entry()
    
       elif choice == 4:
        jm.Delete_Entry()
   
       elif choice == 5:
        print("\nThank you for Using Personal Journal Manager. Goodbye!!\n")
        break
    
        
       elif choice == 6:
        print("Explore Module Attributes:")
        module_name = input("Enter module name to explore: ")

    try:
            module = __import__(module_name)
            attrs = [a for a in dir(module) if not a.startswith("_")]  # clean list

            print(f"Available Attributes in {module_name} module:")
            print(attrs)
            print("===========================")

    except ModuleNotFoundError:
            print("Module not found. Try a valid module name.")
