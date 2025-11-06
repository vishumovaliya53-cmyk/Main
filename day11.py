l = []

def crLi():
     num = int(input("Enter How many Element want you Add :"))

     for i in range(num):
        el = int(input(f"Enter the num f{i + 1} : "))
        l.append(el)
    #  print("\nList Created !")
     return l

def sumLi(l):
    return sum(l)

def Findmax(l):
    return max(l)

def Findmin(l):
    return min(l)

def AvarageLi(l):
    return sum(l)/len(l) if l else 0

def fact(num):
    if num <= 1:
        return 1
    return num * fact(num-1)

      
while True:
     
 print("Enter 1 to create list")
 print("Enter 2 to sum the list")
 print("Enter 3 to find max in the list")
 print("Enter 4 to find min in the list")
 print("Enter 5 to find Avarage in the list")
 print("Enter 6 to find fact in the list")
 print("Enter 7 to Exit")

 choice = int(input("\nEnter your choice : "))  

 if choice==1:
     l = crLi()
     print("\nList Created !" , l)

 elif choice == 2:
    print("Sum of list :", sumLi(l))


 elif choice==3:
      print("Maximum Element : " , Findmax(l))

 elif choice==4:
     print("Minimum Element : " , Findmin(l))

 elif choice==5:
     print("Avarage Element : " , AvarageLi(l))

 elif choice==6:
     num = int(input("Enter a number to find factorial : "))
     result = fact(num)
     print(f"Factorial of {num} is {result}")
     
 elif choice==7:
     print("Exiting !")
     break

 else:
     print("Choice Invalid ! Please Try Again ! ")