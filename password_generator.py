import random
import string

while True:

    print("\n==== PASSWORD GENERATOR ====")

    # User input
    length = int(input("Enter password length: "))

    # Characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    # Display password
    print("Generated Password:", password)

    # Ask user to continue
    again = input("Do you want another password? (yes/no): ")

    if again.lower() != "yes":
        print("Program closed.")
        break

input("Press Enter to exit...")