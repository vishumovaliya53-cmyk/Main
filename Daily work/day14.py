# list comprehension  ----> for create a list

li = [i + 2 for i in range(10)]     # [i + 2 for i in range(10)  if i % 2 == 0] 
print(li)

li2 = []
for i in range(10):
    li2.append(i + 2)
print(li)

a = 10 

def greet ():
    a = 45
    print("Inside function: ",a)

greet()
print("Outside function: ",a)


x = 45
def my_function():
    global x
    x += 62
    print("Inside function: ",x)   

my_function()
print("Outside function: ",x)


a = 100
b = 200

def update_values():
    global a, b
    a += 10
    b -= 20

update_values()
print(a, b)  # Output: 110 180


def outer():
    global x
    x = "Hello"

    def inner():
        global x
        x = "World"

    inner()
    print("Inside outer:", x)

outer()
print("Outside function:", x)


# unpack to tuple
def get_values():
    return 10, 20, 30  # Returns a tuple

result = get_values()
print(result)  # Output: (10, 20, 30)

a, b, c = get_values()
print(a, b, c)  # Output: 10 20 30


def get_student():
    return {"name": "Alice", "age": 20, "grade": "A"}

student = get_student()
print(student["name"], student["age"])  # Output: Alice 20
print(student["name"], student["age"], student["grade"])  # Output: Alice 20 A


def get_numbers():
    return 5, 10

x, y = get_numbers()
print(x, y)  # Output: 5 10




# nested function 

def outer_function():
    def inner_function():
        # Inner function logic
        print("Hello from inner function!")
    
    inner_function()  # Calling the inner function

outer_function()  # Calling the outer function

