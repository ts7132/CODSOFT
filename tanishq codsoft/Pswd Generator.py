import random
import time
import string

def generate_password(length, use_uppercase, use_digits, use_punctuation):
    """Generate a random password of given length with character set preferences"""
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    if not use_uppercase and not use_digits and not use_punctuation:
        characters += string.ascii_lowercase

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_password_length():
    """Get the desired length of the password from the user"""
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 8): "))
            if length < 8:
                print("Password should be at least 8 characters long. Please try again.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_character_set_preferences():
    """Get the character set preferences from the user"""
    use_uppercase = input("Do you want to include uppercase letters in your password? (y/n) ").lower() == 'y'
    use_digits = input("Do you want to include digits in your password? (y/n) ").lower() == 'y'
    use_punctuation = input("Do you want to include punctuation in your password? (y/n) ").lower() == 'y'
    return use_uppercase, use_digits, use_punctuation

def main():
    """The main function to run the password generator"""
    print("\033[1;32mWelcome to the Password Generator!\033[0m")
    time.sleep(1)
    print("\033[1;32mGet ready to generate a strong and secure password!\033[0m")
    time.sleep(1)
    print("\033[1;32mHere we go...\033[0m")
    time.sleep(0.5)

    use_uppercase, use_digits, use_punctuation = get_character_set_preferences()
    length = get_password_length()
    password = generate_password(length, use_uppercase, use_digits, use_punctuation)

    print("\033[1;32mYour randomly generated password is: \033[0m" + "\033[1;31m" + password + "\033[0m")
    time.sleep(1)
    print("\033[1;32mThank you for using the Password Generator!\033[0m")

if __name__ == "__main__":
    main()