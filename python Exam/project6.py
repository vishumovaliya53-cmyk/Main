print()

file = "main.txt"

class filedata:
    def __init__ (self,filename="main.txt"):
        self.filename=filename
        
    def Add_Entry(self,entry):
        with open(self.filename,"a") as file:
            file.write(entry + "\n")
            print("Entry Added successfully !!")
            
    def View_Entry(self):
        try:
            with open(self.filename,"r")as file:
                v=file.read()
                print("\n--- Journal Entries ---\n")

                print(v)
        except FileNotFoundError:
            print("File Not Found!")
            
    def Search_Entry(self):
        s=input("Enter A Keyword for Search: ")
        with open("main.txt","r")as file:
            a=file.readline()
        for line in enumerate(a):
            if s in line:
                print(line)
                
    def Delete_Entry(self):
        with open (self.filename,"w") as file:
            file.write("")
            print("All Journal Entries Deleted !")
            
jm=filedata("main.txt") 

while True:
    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")


    choice = input("\nEnter your choice: ")

    if choice == 1:
            entry = input("Write your journal entry: ")
            jm.Add_Entry(entry)
    elif choice == 2:
            jm.View_Entry()
    elif choice == 3:
            keyword = input("Enter keyword/date to search: ")
            jm.Search_Entry()
    elif choice == 4:
            jm.Delete_Entry()
    elif choice == 5:
            print("Exiting Journal App.")
            break
    else: 
      print("INVALID CHOICE !!")