# Welcome to my Math Quiz
# 9 April 2023
# CTI-110 P5HW - Math Quiz
# Alberto Pajarilla

import random

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def add_numbers():
    num1, num2 = generate_numbers()
    result = num1 + num2
    guess = int(input(f"  {num1}\n+ {num2}\n\nEnter answer. \n"))
    count = 1
    while guess != result:
        if guess < result:
            guess = int(input("Sorry, guess is too low.\n \nTry again: "))
        else:
            guess = int(input("Sorry, guess is too high.\n \nTry again: "))
        count += 1
    print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {count}")

def subtract_numbers():
    num1, num2 = generate_numbers()
    if num1 < num2:
        num1, num2 = num2, num1
    result = num1 - num2
    guess = int(input(f"  {num1}\n- {num2}\n\nEnter answer. \n"))
    count = 1
    while guess != result:
        guess = int(input("Sorry, guess is incorrect.\n \nTry again: "))
        count += 1
    print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {count}")

def display_menu():
    print("\nMAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

def main():
    print("Welcome to Math Quiz!")
    while True:
        display_menu()
        choice = input("\nPlease choose one of the menu options: ")
        if choice == "1":
            add_numbers()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            print("Thank you for playing...\nBye!!")
            break
        else:
            print("\nError: Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
