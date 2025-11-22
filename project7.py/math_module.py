import math

# ------------------------------------------------------
# NEW: Factorial Function
# ------------------------------------------------------
def factorial_value():
    n = int(input("\nEnter number for factorial: "))

    if n < 0:
        print("Factorial not defined for negative numbers.")
    else:
        print(f"Factorial of {n} is:", math.factorial(n))


# ------------------------------------------------------
# NEW: Compound Interest Function
# ------------------------------------------------------
def compound_interest():
    print("\nCompound Interest Calculator")

    p = float(input("Enter Principal Amount (P): "))
    r = float(input("Enter Annual Rate (R %): "))
    t = float(input("Enter Time in Years (T): "))
    n = int(input("Enter number of times interest applied per year (n): "))

    # Formula: A = P * (1 + r/n)^(n*t)
    A = p * (1 + (r / 100) / n) ** (n * t)
    CI = A - p

    print("\n--- Result ---")
    print("Total Amount (A):", round(A, 2))
    print("Compound Interest (CI):", round(CI, 2))
