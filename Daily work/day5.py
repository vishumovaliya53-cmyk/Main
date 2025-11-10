# #pattern

# for i in range(5):
#     print("* "*5)
#     #print("* * * * *")

# for i in range(1 , 6):
#     print(str(i) *5)

# #2

# for i in range(1,6):
#     print("* "*i)

# #3

# for i in range(5):
#     print(str(i)*5)

# #4

# for i in range(1,6):
#     print(str(i)*i)

# #5 neasted loop

# for i in range(1,7):
#     for j in range(1,i):
#         print(j,end=" ")
#     print("\n")
    
# #6 reverse

# for i in range(5,0,1):
#     print("* "*i)

# #7

# for i in range(5,0,-1):
#     print(str(i)*i)



# choice program

while True:
    print("Enter 1 to order pizza")
    print("Enter 2 to order Momos")
    print("Enter 3 to order Maggie")
    print("Enter 4 to order coldrinks")
    print("Enter 0 to Exit")

    print()

    choice = int(input("Enter your choice : "))

    if choice==1:
        while True:
             print("Enter 1 to margerita pizza")
             print("Enter 2 to maxican pizza")
             print("Enter 3 to ittalian pizza")
             print("Enter 4 to Double chease pizza")
             print("Enter 0 to exit!")

             choice = int(input("Enter your choice : "))

             if choice==1:
                 print("you ordered margerita pizza")
             elif choice==2:
                 print("you ordered maxican pizza")
             elif choice==3:
                 print("you ordered ittalian pizza")
             elif choice==4:
                 print("you ordered Double chease pizza")
             elif choice==0:
                 print("Bye")
                 break
             else:
                 print("Invalid choice")

    elif choice==2:
        while True:
            print("Enter 1 to Steam Momos")
            print("Enter 2 to Fried Momos")
            print("Enter 3 to Sezwan Momos")
            print("Enter 4 to Afghani Momos")
            print("Enter 0 to exit!")

            choice = int(input("Enter your choice : "))

            if choice==2:
                 print("you ordered Steam Momos")
            elif choice==2:
                 print("you ordered Fried Momos")
            elif choice==3:
                 print("you ordered Sezwan Momos")
            elif choice==4:
                 print("you ordered Afghani Momos")
            elif choice==0:
                 print("Bye")
                 break
            else:
                 print("Invalid choice")

    elif choice==3:
        while True:
            print("Enter 1 to plane maggie")
            print("Enter 2 to vegitable maggie")
            print("Enter 3 to cheese maggie")
            print("Enter 4 to corn cheese maggie")
            print("Enter 0 to exit!")

            choice = int(input("Enter your choice : "))

            if choice==1:
                 print("you ordered plan maggie")
            elif choice==2:
                 print("you ordered vegitable maggie")
            elif choice==3:
                 print("you ordered cheese maggie")
            elif choice==4:
                 print("you ordered corn cheese maggie")
            elif choice==0:
                 print("Bye")
                 break
            else:
                 print("Invalid choice")

    elif choice==4:
        while True:
            print("Enter 1 to Mazza")
            print("Enter 2 to Sprite")
            print("Enter 3 to Pepsi")
            print("Enter 4 to Limca")
            print("Enter 0 to exit!")

            choice = int(input("Enter your choice : "))

            if choice==1:
                 print("you ordered Mazza")
            elif choice==2:
                 print("you ordered Sprite")
            elif choice==3:
                 print("you ordered Pepsi")
            elif choice==4:
                 print("you ordered Limca")
            elif choice==0:
                 print("Bye")
                 break
            else:
                 print("Invalid choice")
     
    else:
         print("Thanks for visiting")