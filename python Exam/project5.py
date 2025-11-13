
print("\n--- Python OOP Project: Employee Management System ---")
 
class Employee:
    def __init__(self,name,__emp_id,age,__salary):
         self.emp_id=__emp_id
         self.name=name
         self.age=age
         self.salary=__salary

    def getdata(self):
          print(f"Name:{self.name},ID:{self.emp_id},Age:{self.age},Salary:{self.salary}")

class Manager(Employee):
     def __init__(self,emp_id,name,age,salary,):
          super().__init__(self,name,emp_id,age)
          self.salary=salary

     def getdata(self):
          print(f"Name:{self.name},Id:{self.emp_id},Age:{self.age},Salary:{self.salary}")

class Developer(Employee):
    def __init__(self,emp_id,name,age,salary,department,programming_lang):
          super().__init__(name,emp_id,age,salary)
          self.department=department
          self.programming_lang=programming_lang

    def getdata(self):
          print(f"Name:{self.name},Id:{self.emp_id},Age:{self.age},Salary:{self.salary},Department:{self.department},Programming:{self.programming_lang}")

employee=[]
manager=[]
developer=[]

while True:
     print("\n---Choose another operation---")
     print("\n1.Create a Employee: ")
     print("2.Create an Employee: ")
     print("3.Create a Manager: ")
     print("4.View Details: ")
     print("5.EXIT")


     choice=int(input("\nENTER YOUR CHOICE:- "))

     if choice==1:
          name=input("\nEnter Name: ")
          age=int(input("Enter Age: "))
          id=int(input("Enter ID: "))
          salary=int(input("Enter Employee Salary: $"))
          e=Employee(name,age,id,salary)
          employee.append(e)
          print(f"\nEmployee create with name:{name}, age:{age}, ID:{id} and salary:{salary}")

     elif choice==2:
        name=input("\nEnter Name: ")
        id=input("Enter id: ")
        age=int(input("Enter Age: "))
        salary=float(input("Enter Manager Salary: $"))
        m=Manager(name,id,age,salary)
        manager.append(m)
        print(f"\nManager created with name:{name}, id:{id}, age:{age}, salary:{salary}.")

     elif choice==3:
          name=input("\nEnter Name: ")
          id=input("Enter id: ") 
          age=int(input("Enter Age: "))
          salary=float(input("Enter Person Salary: $"))
          department=input("Enter Department: ")
          programming=input("Enter programming language: ")
          d=Developer(name,id,age,salary,department,programming)
          developer.append(d)
          print(f"\nDeveloper created with name:{name}, id:{id}, age:{age}, salary:{salary}, departmnet:{department}, programming_lang:{programming}.")

     elif choice==4:
        print("\nchoose Details to show:\n")
        print("1.Employee")
        print("2.Manager")
        print("3.Developer")
        
        ch = int(input("\nEnter your choice: "))
        
        if ch == 1:
            print("\nEmployee Details: ")
            for e in employee:
                e.getdata()
                
        elif ch == 2:
            print("\nManager Details: ")
            for m in manager:
                m.getdata()
                
        elif ch == 3:
            print("\nDeveloper Details: ")
            for d in developer:
                d.getdata()
    
        else:
            print("Invalid choice!")        

     elif choice==5:
           print("\nExiting the system. All resources have been freed")
           break
     
     else:
       print("\nInvalid Choice!")

print("\nGoodbye!")