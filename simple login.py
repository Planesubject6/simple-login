import os
import time
import random
import string

ACCOUNTS_FILE = "accounts.txt"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(seconds):
    time.sleep(seconds)


def read_accounts():
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if ',' in line:
                    username, password = line.split(',', 1)
                    accounts[username] = password
    return accounts


def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as f:
        for username, password in accounts.items():
            f.write(f"{username},{password}\n")


def login(accounts):
    username = input("Username: ")
    password = input("Password: ")
    if username in accounts and accounts[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


def generate_password(length=8,
                      use_numbers=True,
                      use_symbols=True,
                      use_letters=True):
    characters = ''
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_letters:
        characters += string.ascii_letters
    if not characters:
        characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))


def register(accounts):
    username = input("Choose a username: ")
    if username in accounts:
        print("Username already exists.")
        return

    choice = input("Do you want to generate a password (yes/no)? ")
    if choice.lower() == 'yes':
        length = int(input("Enter password length (default is 8): ") or "8")
        use_numbers = input("Include numbers (yes/no)? ").lower() == 'yes'
        use_symbols = input("Include symbols (yes/no)? ").lower() == 'yes'
        use_letters = input("Include letters (yes/no)? ").lower() == 'yes'
        password = generate_password(length, use_numbers, use_symbols,
                                     use_letters)
        print(f"Generated password: {password}")
    else:
        password = input("Enter your password: ")

    accounts[username] = password
    save_accounts(accounts)
    print("User registered successfully.")


def view_accounts(accounts):
    for username, password in accounts.items():
        print(f"Username: {username}, Password: {password}")


def main():
    accounts = read_accounts()
    while True:
        clear_screen()
        print("Menu:")
        print("1. Login")
        print("2. Register")
        print("3. View accounts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            login(accounts)
        elif choice == '2':
            register(accounts)
        elif choice == '3':
            view_accounts(accounts)
        elif choice == '4':
            print("Exiting...")
            pause(2)
            break
        else:
            print("Invalid choice.")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
