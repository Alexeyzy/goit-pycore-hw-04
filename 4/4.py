import sys

from pathlib import Path
from colorama import Fore, Style

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return f"name {name} not found"
    else:    
        contacts[name] = phone
    return "Contact updated." 

def show_phone(args, contacts):
    name, = args
    if name not in contacts:
        return f"name {name} not found"
    else:    
        return f"{contacts[name]}"

def show_all(contacts):
    res = [f"{key} {value}" for key, value in contacts.items()]
    return "\n".join(res)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}

    print("Welcome to the assistant bot! \n \
    - add [ім'я] [новий номер телефону] \n \
    - change [ім'я] [новий номер телефону] \n \
    - phone [ім'я] [новий номер телефону] \n \
    - all \n \
    - close or exit")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)      
        if command in ["close", "exit"]:
            print("Good bye!")
            break      
        elif command == "hello":
            print("How can I help you?")      
        elif command == "add":
            print(Fore.GREEN + add_contact(args, contacts), Style.RESET_ALL)           
        elif command == "change":
            print(Fore.GREEN + change_contact(args, contacts), Style.RESET_ALL)       
        elif command == "phone":
            print(Fore.GREEN + show_phone(args, contacts), Style.RESET_ALL)         
        elif command == "all":
            print(Fore.GREEN + show_all(contacts), Style.RESET_ALL)
        else:
            print("Invalid command.")
        
        print(" - add [ім'я] [новий номер телефону] \n \
- change [ім'я] [новий номер телефону] \n \
- phone [ім'я] [новий номер телефону] \n \
- all \n \
- close or exit")

if __name__ == "__main__":
    main()