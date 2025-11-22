import random

def random_number():
    print("Random Number:", random.randint(1, 100))


def random_list():
    fruits = ["apple", "banana", "kiwi", "mango", "orange"]
    result = random.sample(fruits, 3)
    print("Random List:", result)
    return result


def generate_otp():
    otp = "".join(str(random.randint(0, 9)) for _ in range(6))
    print("Generated OTP:", otp)


def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    pool = letters + letters.upper() + numbers + symbols
    password = "".join(random.choice(pool) for _ in range(10))

    print("Generated Password:", password)
