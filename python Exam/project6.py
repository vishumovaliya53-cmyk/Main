
print("\nWelcome To The Journal Manager!")

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
    
    else:
        print("\nInvalid Option. Please select a valid Option!")