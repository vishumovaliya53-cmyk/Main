import numpy as np

print("\nWelcome to the numpy Analyzer !")
print("===============================")

# --------------------------------------------------------
# 1. ARRAY CREATION
# --------------------------------------------------------
            
def create_array():
    print("\nSelect the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")     

    choice = int(input("Enter your choice: "))

    # ------------------ 1D ARRAY ------------------
    if choice == 1:
        size = int(input("Enter number of elements: "))
        elements = list(map(int, input("Enter elements separated by space: ").split()))
        arr = np.array(elements)
        print("\n1D Array created successfully!")
        print(arr)
        return arr

    # ------------------ 2D ARRAY ------------------
    elif choice == 2:
        rows = int(input("\nEnter rows: "))
        cols = int(input("Enter columns: "))

        print("\nEnter 6 elements for the array separated by space:")
        elements = list(map(int, input().split()))

        arr = np.array(elements).reshape(rows, cols)
        print("\n2D Array created successfully!")
        print(arr)
        return arr


    # ------------------ 3D ARRAY ------------------
    elif choice == 3:
        depth = int(input("Enter depth (number of matrices): "))
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        total = depth * rows * cols
        print(f"\nEnter {total} elements separated by space:")
        elements = list(map(int, input().split()))

        arr = np.array(elements).reshape(depth, rows, cols)
        print("\n3D Array created successfully!")
        print(arr)
        return arr

    else:
        print("Invalid choice!")



# --------------------------------------------------------
# 2. MATHEMATICAL OPERATIONS
# --------------------------------------------------------

def mathematical_operations(arr):
    print("\nMathematical operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Indexing")
    print("6. Slicing")
    print("7. Go Back")

    choice = int(input("Enter your choice: "))
    n = int(input("Enter number: "))

    if choice == 1:
        print(arr + n)
    elif choice == 2:
        print(arr - n)
    elif choice == 3:
        print(arr * n)
    elif choice == 4:
        print(arr / n)
    elif choice == 5:
        idx = tuple(map(int, input("Enter index (e.g., 1 2 for 2D, 0 1 2 for 3D): ").split()))
        print("\nIndexed Value:", arr[idx])
    elif choice == 6:
        slice_input = input("Enter slicing indices (e.g., 0:2,1:3 for 2D): ")
        slice_parts = slice_input.split(',')
        slices = []
        for part in slice_parts:
            start, end = map(int, part.split(':'))
            slices.append(slice(start, end))
        print("\nSliced Array:")
        print(arr[tuple(slices)])
    elif choice == 7:
        return
    else:
        print("Invalid choice!")
        
# --------------------------------------------------------
# 3. COMBINE ARRAYS
# --------------------------------------------------------

def combine_arrays(arr):
        print("\nCombine arrays:")
        print("1. Horizontal combine")
        print("2. Vertical combine")
        
        ch = int(input("Enter your choice: "))

        print("Enter elements for another array:")
        arr2 = list(map(int, input("Enter elements: ").split()))
        arr2 = np.array(arr2)
        arr_flat = arr.reshape(1, -1)
        arr2_flat = arr2.reshape(1, -1)

        if ch == 1:
           print("\nCombined (Horizontal):")
           print(np.hstack((arr_flat, arr2_flat)))

        elif ch == 2:
           print("\nCombined (Vertical):")
           print(np.vstack((arr_flat, arr2_flat)))

        else:
           print("Invalid choice!")
        

# --------------------------------------------------------
# 4. SPLIT ARRAYS
# --------------------------------------------------------

def split_array(arr):
    print("\nSplit array:")
    print("1. Horizontal split")
    print("2. Vertical split")
    print("3. Go Back")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        cols = arr.shape[1]
        if cols % 2 != 0:
            print(np.array_split(arr, 2, axis=1))
        else:
            print(np.hsplit(arr, 2))

    elif choice == 2:
        rows = arr.shape[0]
        if rows % 2 != 0:
            print(np.array_split(arr, 2, axis=0))
        else:
            print(np.vsplit(arr, 2))
    
    elif choice == 3:
        return
    
    else:
        print("Invalid choice!")

        

# --------------------------------------------------------
# 5. SEARCH, SORT, FILTER
# --------------------------------------------------------

def search_sort_filter(arr):
    print("\nSearch, Sort and Filter:")
    print("1. Search element")
    print("2. Sort array")
    print("3. Filter array")
    print("4. Go Back")

    choice = int(input("Enter  your choice: "))

    if choice == 1:
        x = int(input("Enter element to search: "))
        positions = np.where(arr == x)
        print("Positions:", positions)

    elif choice == 2:
        print("Sorted array:", np.sort(arr, axis=None))

    elif choice == 3:
        limit = int(input("Show elements greater than: "))
        print(arr[arr > limit])
        
    elif choice == 4:
        return

    else:
        print("Invalid choice!")


# --------------------------------------------------------
# 6. AGGREGATION / STATISTICS
# --------------------------------------------------------

def aggregation_functions(arr):
    print("\nChoose aggregation/statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Max")
    print("5. Min")
    print("6. Go Back")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Sum =", np.sum(arr))
    elif choice == 2:
        print("Mean =", np.mean(arr))
    elif choice == 3:
        print("Median =", np.median(arr))
    elif choice == 4:
        print("Max =", np.max(arr))
    elif choice == 5:
        print("Min =", np.min(arr))
    elif choice == 6:
        return
    else:
        print("Invalid choice!")

# --------------------------------------------------------
# MAIN MENU
# --------------------------------------------------------

def main():
    arr = None

    while True:
        print("Choose an option:")
        print("1. Create a Numpy array")
        print("2. Perform Mathematical operations")
        print("3. Combine Array")
        print("4. Split Array")
        print("5. Search , sort , filter arrays")
        print("6. Compute aggregation / statistical")
        print("7. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            arr = create_array()

        elif choice == 2:
            mathematical_operations(arr)

        elif choice == 3:
            combine_arrays(arr)
            
        elif choice == 4:
            split_array(arr)

        elif choice == 5:
            search_sort_filter(arr)
            
        elif choice == 6:
            aggregation_functions(arr)

        elif choice == 7:
            print("Thank you for using the Numpy Multitool!")
            break

        else:
            print("Please create an array first!")


# Run program
if __name__ == "__main__":
    main()
