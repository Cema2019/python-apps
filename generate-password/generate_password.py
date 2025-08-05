import secrets
import string
import random

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    if length < nums + special_chars + uppercase + lowercase:
        raise ValueError("Length too short for the required constraints")

    # Character set
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = upper_letters + lower_letters + digits + symbols

    password_chars = []

    # Add required number of characters
    password_chars += [secrets.choice(digits) for _ in range(nums)]
    password_chars += [secrets.choice(symbols) for _ in range(special_chars)]
    password_chars += [secrets.choice(upper_letters) for _ in range(uppercase)]
    password_chars += [secrets.choice(lower_letters) for _ in range(lowercase)]

    # Fill the rest of the password with random choices from all characters
    remaining_length = length - len(password_chars)
    password_chars += [secrets.choice(all_chars) for _ in range(remaining_length)]

    # Shuffle to avoid predictable order
    random.shuffle(password_chars)

    return ''.join(password_chars)


if __name__ == "__main__":
    pwd = generate_password()
    print("Generated password:", pwd)
