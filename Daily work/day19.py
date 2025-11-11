# # #file handling allows us to read , write , and modify files in python.

# # #python provides built in functions like open() , read() , write() , and close()
# # #for file operation

# # # * MODE

# # # 1."r" :- "Read File"
# # # 2."w" :- "write file"
# # # 3."a" :- "Appened file"
# # # 4."x" :- "Create file"
# # # 5."b" :- "Binory file"
# # # 6."t" :- "Text file"

# # # Read Mode :- File create karni hogi

print("\nWelcome To File Handling !\n")

while True:
    
    print("1.Enter X To Create File: ")
    print("2.Enter R To Read file: ")
    print("3.Enter W To write File: ")
    print("4.Enter A To Add something in File: ")
    print("5.Enter E Exiting: ")

    choice = (input("\nEnter Your Requirement : "))

    if choice == "X":
        file_name = str(input("\nEnter your File Name: "))
        print("\nCreate your own file : \n")

        with open(file_name , "x") as file:
            print(f"File {file_name} Created Successfully !")

    
    elif choice == "R":
        file_name = str(input("\nEnter File Name To Read: "))

        with open(file_name,"r") as file :
            print(file.read())

    elif choice=="W":
        file_name = input("Enter your file name: ")

        with open(file_name, "w") as file:
            data = input("\nEnter Data to your File: ")
            file.write(data)

    elif choice == "A":       
        file_name = input("Enter file name to append :")

        with open(file_name,"a") as file:
            data2=input("Enter data to add in your Append file: ")
            file.write("\n"+ data2)

    elif choice == "E":
        print("Exiting To filehandling !")
        break

    else:
        print("Invalid Requirement!")
