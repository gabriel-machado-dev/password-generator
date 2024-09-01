import random
import string
import os

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Define character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

print(CYAN + BOLD + r'''

              ░█▀█░█▀█░█▀▀░█▀▀░█░█░█▀█░█▀▄░█▀▄░░░█▀▀░█▀▀░█▀█░█▀▀░█▀▄░█▀█░▀█▀░█▀█░█▀▄
              ░█▀▀░█▀█░▀▀█░▀▀█░█▄█░█░█░█▀▄░█░█░░░█░█░█▀▀░█░█░█▀▀░█▀▄░█▀█░░█░░█░█░█▀▄
              ░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀░░░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀

''' + RESET)

def instructions():
    print(f"{YELLOW}Instructions:{RESET}")
    print(f"{YELLOW}1. Enter the desired password length by typing a number greater than zero.{RESET}")
    print(f"{YELLOW}2. Select at least one character sets to include in the password by typing 'yes' or 'no'{RESET}")
    print(f"{YELLOW}3. The password will be generated and displayed on the screen.{RESET}")
    print(f"{YELLOW}4. You can generate another password or exit the program.{RESET}\n")

# Get user inputs
def get_inputs() -> tuple[int, bool, bool, bool, bool]:
    def get_boolean_input(prompt: str) -> bool:
        while True:
            response = input(prompt).strip().lower()
            if response in ['yes', 'no']:
                return response == 'yes'
            else:
                print("Invalid input, please type 'yes' or 'no'.")

    try:
        length = int(input("Enter the desired password length: "))

        if length <= 0:
            print("Invalid input, please enter a number greater than 0.")
            return get_inputs()

        print(f"{GREEN} Select the character sets to include in the password, type 'yes' to include a set or 'no' to exclude it.{RESET}\n")
        include_uppercase = get_boolean_input("Include uppercase letters? (yes/no): ")
        include_lowercase = get_boolean_input("Include lowercase letters? (yes/no): ")
        include_digits = get_boolean_input("Include digits? (yes/no): ")
        include_symbols = get_boolean_input("Include symbols? (yes/no): ")

        if any([include_uppercase, include_lowercase, include_digits, include_symbols]):
            return length, include_uppercase, include_lowercase, include_digits, include_symbols
        else:
            print("No character sets selected, please select at least one.")
            return get_inputs()

    except ValueError:
        print("Invalid input, please enter a number.")
        return get_inputs()

# Combine selected character sets
def get_all_characters(include_uppercase: bool, include_lowercase: bool, include_digits: bool, include_symbols: bool) -> str:
    all_characters = ''
    if include_uppercase:
        all_characters += uppercase
    else:
        print(f"{RED}No uppercase letters selected, password strength reduced.{RESET}")
    if include_lowercase:
        all_characters += lowercase
    else:
        print(f"{RED}No lowercase letters selected, password strength reduced.{RESET}")
    if include_digits:
        all_characters += digits
    else:
        print(f"{RED}No digits selected, password strength reduced.{RESET}")
    if include_symbols:
        all_characters += symbols
    else:
        print(f"{RED}No symbols selected, password strength reduced.{RESET}")

    return all_characters

# Generate password
def main():
    length, include_uppercase, include_lowercase, include_digits, include_symbols = get_inputs()

    os.system('cls' if os.name == 'nt' else 'clear')

    all_characters = get_all_characters(include_uppercase, include_lowercase, include_digits, include_symbols)
    if len(all_characters) == 0:
        print(f"No characters selected, password cannot be generated.")
        return

    # Generate password
    password = ''.join(random.sample(all_characters, length))
    print(f"Generated password: {MAGENTA + BOLD}{password}{RESET}")

if __name__ == '__main__':
    while True:
        instructions()
        main()

        response = input(f"{YELLOW}Do you want to generate another password? (yes/no): {RESET}").strip().lower()
        if response != 'yes':
            break
        os.system('cls' if os.name == 'nt' else 'clear')
