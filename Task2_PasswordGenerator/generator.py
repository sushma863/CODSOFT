import random
import string

def generate_password(length, complexity):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Complexity Options
    if complexity == "1":
        characters = lowercase

    elif complexity == "2":
        characters = lowercase + uppercase + digits

    elif complexity == "3":
        characters = lowercase + uppercase + digits + symbols

    else:
        characters = lowercase + uppercase

    # Generate Password
    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    return password