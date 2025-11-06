
print("\nWelcome to the Student Data Organizer !")

students = []

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display all Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        print("\nEnter student details :")
        st = {
            "id": int(input("Student ID : ")),
            "Name": input("Name : "),
            "Age": int(input("Age : ")),
            "Grade": input("Grade : "),
            "Dob": input("Date of Birth (dd-mm-yyyy) : "),
            "Subjects": input("Subjects (comma-separated) : ")
        }
        students.append(st)
        print("\nStudent added successfully !")

    elif choice == 2:
        if len(students) == 0:
            print("\nNo student records found !")
        else:
            print("\n--- Display All Students ---")
            for st in students:
                print(f"Student ID : {st['id']} | Name : {st['Name']} | Age : {st['Age']} | Grade : {st['Grade']} | DOB : {st['Dob']} | Subjects : {st['Subjects']}")

    elif choice == 3:
        update = int(input("\nEnter student ID to update : "))
        for st in students:
            if st["id"] == update:
                st["Name"] = input("New Name : ")
                st["Age"] = int(input("New Age : "))
                st["Grade"] = input("New Grade : ")
                st["Dob"] = input("New Date of Birth (dd-mm-yyyy) : ")
                st["Subjects"] = input("New Subjects (comma-separated) : ")
                print("\nStudent updated successfully !")
                


    elif choice == 4:
        delete = int(input("\nEnter student ID to delete : "))
        for st in students:
            if st["id"] == delete:
                students.remove(st)
                print("Student deleted successfully !")
                
        else:
            print("Student not found !")

    elif choice == 5:

        StudentID = int(input("Enter student id to print students subject: "))

        for st in students:

           if st["id"]== id:

               print(f"display all subjects = {st['Subjects (comma-separated)']}\n")

                    


    elif choice == 6:
        print("\nThank you for using the Student Data Organizer !\n")
        break

    else:
        print("\nInvalid choice! Please try again.\n")


