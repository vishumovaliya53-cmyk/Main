class Car:
    def __init__ (self , seat , tyre):
        self.seat = seat
        self.tyre = tyre

class toyota(Car):
    def __init__(self , seat , tyre , AC):
        super().__init__(seat , tyre)
        self.AC = AC

    def getdata(self):
        print(f"The Features are seat -> {self.seat} , Tyre -> {self.tyre} , Ac -> {self.AC}")

class mahindra(Car):
    def __init__(self , seat , tyre , supersuspension):
        super().__init__(seat , tyre)
        self.supersuspension = supersuspension

    def getdata(self):
         print(f"The Features are seat -> {self.seat} , Tyre -> {self.tyre} , Supersuspension -> {self.supersuspension}")

toyotacars=[]
mahindracars=[]

while True:

    print("\n Welcome!\n")

    print("Enter 1 to add Toyota cars : ")
    print("Enter 2 to add Mahindra cars : ")
    print("Enter 3 to add View cars : ")
    print("Enter 0 to Exit : \n ")

    choice = int(input("Enter your choice : "))

    if choice==1:
        seat = int(input("Enter the number of seats : "))
        tyre = int(input("Enter the number of tyres : "))
        AC = input("Enter the availibility of AC(Y/N) : ")

        tobj = toyota(seat,tyre,AC)

        toyotacars.append(tobj)

    elif choice==2:
        seat = int(input("Enter the number of seats : "))
        tyre = int(input("Enter the number of tyres : "))
        AC = input("Enter the availibility of supersuspension : ")

        mobj = mahindra(seat,tyre,AC)

        mahindracars.append(mobj)

    elif choice==3:
        print("Enter 1 to show Toyota cars")
        print("Enter 2 to show mahindra cars")

        ch = int(input("Enter your choice : "))

        if ch==1:
            for obj in toyotacars:
                obj.getdata()

        elif ch==2:
            for obj in mahindracars:
                obj.getdata()

        else:
            print("Choice is Wrong!❌")

    elif choice==0:
        print("Exiting!")
        break

    else:
        print("INVALID CHOICE!❌")