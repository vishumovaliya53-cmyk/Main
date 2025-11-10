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

inova = toyota(7 , 4 , "Available")
XUV = toyota(5 , 4 , "Available")

 