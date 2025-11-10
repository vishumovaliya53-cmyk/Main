students = []

while True:

    print("\n Welcome to the Programme ! \n")

    print("1. Add")
    print("2. Read")
    print("3. Delete")
    print("4. Update")
    print("0. Exit")

    choice = int(input("Enter your Choice : "))

    print()

    if choice==1:
        st = {
            "stId" : int(input("Enter Student Id : ")),
            "Name" : input("Enter Student Name : "),
            "City" : input("Enter Student city : "),       
            }
        
        students.append(st)

        print("\n Student Added successfully ! \n")

    elif choice==2:
        for st in students:
         print(f"student Id : " (st("stId")) , "Student Name : " (st("Name")) , "Student City : " (st("City")))


    elif choice==3:
       stId = int(input("Enter Student Id : "))
       for st in students:
          if st ["stId"] == stId:
             students.remove(st)
             print("Student Removed !")
          else:
             print("Student Not found !")

    elif choice==4:
       stId = int(input("Enter Student Id : "))
       for st in students:
          if st ["stId"] == stId:
             st ["name"] = input("Enter the new Name : ")
             st ["City"] = input("Enter the new City : ")
             print("Programme Updated ! \n")
        
    elif choice == 0:
       print("Exiting !")
       break
    else:
       print("Invalid")