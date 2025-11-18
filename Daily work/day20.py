 # Exception Handling
 
 # An Exception is an error that occurs during of a program , disrupting the normal flow
 
 # Types of exeception
 
 # 1.zerodivisionError
 # 2.valueError
 # 3.NameError
 # 4.TypeError
 # 5.IndexError
 # 6.KeyError
 # 7.FilenotfoundError 
 
 # Example:
 
# print("Hello")
# print("Python")
# print(5/0)
# try:
#     print(5/0)
# except:
#     print("Not Divisable")
# print("Hello")
# print("World")

# Don't know error

try:
    print(5/0)
except Exception:
    print("Not Divisable")
    
# Try --- Except --- Else

# The Else Block Returns only if no exception occurs

try:
    print(6/2)
except Exception:
    print("Not Divisable")
else:
    print("There is no error")

# Try --- Exception --- Finally

# The Finally Block always runs , whether an exception occurs or not

finally:
    print("All Above Excuted !!")
    
# KeyWord

# Raise Keyword

a = 10

if a>2:
    raise custom("This is custom Error")