# syntax : [expression for item in iterable if condition]

my_sum = [x**2 for x in range(5)]
print(my_sum)

even_number =[ i for i in range(15) if i % 2 == 0]
print(even_number)

# 1D array means vactor 

arr = [10, 20, 30, 40, 50, 60, 70]

print(arr[1:4])   # Elements from index 1 to 3 
print(arr[:3])    # First 3 elements
print(arr[2:])    # From index 2 to end 
print(arr[::2])   # Every second element , it means gap of index
print(arr[::-1])  # Reverse the array


#CRUD operation

#creat
arr = []  # Empty list
arr.append(10)  # Add element
arr.append(20)
arr.append(30)
print(arr)  # Output: [10, 20, 30]

#update
arr.insert(1, 15)  # Insert 15 at index 1
print(arr)  # Output: [10, 15, 20, 30]
arr[1] = 25  # Change value at index 1
print(arr)

arr.extend([40, 50])  # Add multiple elements
print(arr)

#read
print(arr[2])  # Access element at index 2 → Output: 20
print(arr[0:3])  # Access elements from index 0 to index 2 → Output: [10, 15, 20]

#delete
arr.pop(2)  # Removes element at index 2
print(arr)  # Output: [10, 25, 30, 40, 50]

arr.remove(40)  # Removes first occurrence of 40
print(arr)  # Output: [10, 25, 30, 50]

del arr[1]  # Delete element at index 1
print(arr)  # Output: [10, 30, 50]

arr.clear()  # Removes all elements
print(arr)



# loop in 1D
arr = [10, 20, 30, 40, 50, 60, 70]
for elem in arr:
  print(elem)
  
  

#sorting

arr = [50, 10, 40, 30, 20]

arr.sort()  # Sort in ascending order
print(arr)

arr.sort(reverse=True) # Sort in decending order
print(arr)


arr = [50, 10, 40, 30, 20]

new_arr = sorted(arr)  # Ascending order
print(new_arr)  # Output: [10, 20, 30, 40, 50]
print(arr) 

desc_arr = sorted(arr, reverse=True)
print(desc_arr)  # Output: [50, 40, 30, 20, 10]    



arr = [53, 27, 81, 42, 19]

arr.sort(key=lambda x: x % 10)  # Sort by last digit
print(arr)  # Output: [81, 42, 53, 19, 27]



#sortin string

names = ["Zara", "Alice", "John", "Bob"]

names.sort()
print(names)  # Output: ['Alice', 'Bob', 'John', 'Zara']

names.sort(reverse=True)
print(names)



# Sorting a List of Tuples

students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]

students.sort(key=lambda x: x[0])  # Sort by names (1st element) # output: [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
students.sort(key=lambda x: x[1])  # Sort by marks (2nd element) # Output: [('Bob', 75), ('Charlie', 85), ('Alice', 90)]
print(students)

# 2d array means matrix

matrix = [        
    [1, 2, 3],    
    [4, 5, 6],  
    [7, 8, 9],
]
                      
print(matrix)  

print(matrix[1][1]) # first 1 is raw's index and second 1 is for colum's index and output : 5
print(matrix[-1][1])


# CRUD in 2d array it means matrix

#Creat
matrix.append([10, 11, 12])  
print(matrix) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


#Read
for row in matrix:
    print(row)  # Prints each row
   
    
#Delete
del matrix[1][2]  # Removes element at row 1, column 2
print(matrix) # Output: [[1, 2, 3], [4, 5], [7, 8, 9], [10, 11, 12]]

matrix.pop(1)  # Removes row at index 1
print(matrix)  # Output: [[1, 2, 3], [7, 8, 9], [10, 11, 12]]



for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
    
    
for col in range(len(matrix[0])):  
    for row in matrix:
        print(row[col], end=" ")
    print()
    

# sorting

matrix.sort(key=lambda x: x[0])
print(matrix)




# 3D array

thirdy_array =  [        
   [ [1, 2, 3],    
    [4, 5, 6],  
    [7, 8, 9]
   ]
[       
    [11, 12, 13],    
    [14, 15, 16],  
    [17, 18, 19],
]
]

print(matrix)
print(matrix[1][2])