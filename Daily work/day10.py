# types of functions

# 1.Build in functions
# 2.user Defined Functions (UDF)

# sort :- original list return
# sorted :- new list return

# 2.UDF 
def greet():
    print("name")
    print("Age")
greet()

# 4 types of user define functions
# 1.tnrn 
# 2.tsrn
# 3.tnrs
# 4.tsrs

def name(name):
    print("Hello", name)
greet("name")
     
def add(a,b):
    return a+b
result = add(23,23)
b=34 + result

#default argue
def greet(name , age = 18):
    print(f"name : {name} , age : {age}")

greet("sumit")
greet("Rahul" , 33)

# Non Keywords args

def add(*args):
    print(type(args))
    return sum (args)
result = add (34 , 56 , 57)

print(result)

#key args

