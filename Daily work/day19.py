#file handling allows us to read , write , and modify files in python.

#python provides built in functions like open() , read() , write() , and close()
#for file operation

# * MODE

# 1."r" :- "Read File"
# 2."w" :- "write file"
# 3."a" :- "Appened file"
# 4."x" :- "Create file"
# 5."b" :- "Binory file"
# 6."t" :- "Text file"

# Read Mode :- File create karni hogi

while True:

    print("\nCreate your own file : \n")
    print("1.Enter X To Create File: ")
    print("2.Enter R To Read file: ")
    print("3.Enter W To write File: ")
    print("4.Enter A To Add something in File: ")
    print("5.Enter E Exiting: ")

    choice = (input("\nEnter Your Requirement : "))

    if choice == "X":
        file_name = str(input("\n Enter your File Name: "))

        with open(file_name , "x") as file:
            print(f"File {file_name} Created Successfully !")

    
    elif choice == "R":
        file_name = str(input("\n Enter File Name To Read: "))

        with open(file_name,"r") as file :
            print("\n your content -------")
            print(file.read())

    elif choice=="w":
        file_name = input("Enter Something in file")

        with open(file_name, "w") as file:
            data = input("\nEnter Data to your File :\n")
            file.write(data)

    elif choice == "A":       
        file_name = input("Enter file name to append :")

        with open(file_name,"a") as file:
            data2=input("Enter data to add in oyur exixting file")
            file.write("\n"+ data2)

    elif choice == "E":
        print("Exiting To filehandling !")
        break

    else:
        print("Invalid Reqquirement!")