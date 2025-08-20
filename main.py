#  All Python Programs Combined
import turtle
from random import *

print("=" * 50)
print("PYTHON PROGRAMMING COLLECTION")
print("=" * 50)

# ১. ফাইল অপারেশন (File Operations)
def file_operations():
    print("\n1. FILE OPERATIONS:")
    print("-" * 20)
    try:
        f = open('/storage/emulated/0/Download/code.txt', 'a')
        f.write('\nWelcome back')
        f.close()
        print("File written successfully!")
    except Exception as e:
        print(f"File operation error: {e}")

# ২. ক্লাস এবং অবজেক্ট (Class and Objects)
def class_examples():
    print("\n2. CLASS AND OBJECTS:")
    print("-" * 20)
    
    # Print function
    def p(n=''):
        return print(n)

    class Student:
        name = 'Rashed'
        age = '17'
        roll = 56
        
        def info(self):
            print(f'My name {self.name}')

    s1 = Student()
    p(s1.name)
    s1.info()

def basic_concepts():
    print("\n3. BASIC PROGRAMMING CONCEPTS:")
    print("-" * 20)
    
    # Lists and Dictionaries
    my_list = [1, 2, 3, "hello"]
    print("List:", my_list)
    
    my_dict = {"name": 'Yeasin', "age": 30}
    print(f"Name: {my_dict['name']}, Age: {my_dict['age']}")
    
    my_list = [1, 2, 3, 4, 5]
    print(f"List[-4]: {my_list[-4]}")  # Output: 2
    
    # List comparison
    a = [2, 3, 4]
    b = [2, 3, 4]
    c = a
    
    print(f"a == b: {a == b}")  # True
    print(f"a is b: {a is b}")  # False
    print(f"a is c: {a is c}")  # True
    
    # Lambda function
    double = lambda x: x * 2
    print(f"Double of 10: {double(10)}")
    print(f"Double of 5: {double(5)}")
    
    # Generator function
    def my_generator():
        for i in range(5):
            yield i
    
    print("Generator output:")
    for num in my_generator():
        print(num, end=" ")
    print()
    
    # Decorator
    def my_decorator(func):
        def wrapper():
            print("Before function call")
            func()
            print("After function call")
        return wrapper

    @my_decorator
    def my_function():
        print("Inside the function")

    my_function()
    
    # Number processing
    Number = sum(range(5, 15, 2))
    print(f"Sum result: {Number}")
    while Number in range(50):
        if Number != 45:
            print(Number * 2, end=' ')
        Number += 1
    print('<= The loop is finished')
    
    # Even/Odd separation
    number = [2, 6, 9, 8, 4, 88, 99, 663, 44, 25, 38, 69, 14, 28, 36, 25, 35, 33, 5]
    even = []
    odd = []
    for n in number:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    print(f"Odd numbers: {odd}")
    print(f"Even numbers: {even}")

# ৪. পাসওয়ার্ড ট্র্যাকার (Password Tracker)
def password_tracker():
    print("\n4. PASSWORD TRACKER:")
    print("-" * 20)
    print("Warning: This is a brute force password cracker demonstration.")
    print("Note: This may take a very long time for complex passwords!")
    
    choice = input("Do you want to run password tracker? (y/n): ").lower()
    if choice == 'y':
        User_password = input("Enter a simple password (max 3 characters recommended): ")
        password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        guess = ""
        attempts = 0
        max_attempts = 1000  # Limit attempts to prevent infinite loop
        
        while (guess != User_password) and attempts < max_attempts:
            guess = ""
            for letter in range(len(User_password)):
                guess_letter = password[randint(0, len(password) - 1)]
                guess = str(guess_letter) + str(guess)
            print(f"Attempt {attempts + 1}: {guess}")
            attempts += 1
        
        if guess == User_password:
            print(f"Your Password is = {guess}")
        else:
            print("Password not found within attempt limit.")

# ৫. টার্টল গ্রাফিক্স (Turtle Graphics)
def turtle_graphics():
    print("\n5. TURTLE GRAPHICS:")
    print("-" * 20)
    choice = input("Do you want to run turtle graphics? (y/n): ").lower()
    if choice == 'y':
        try:
            color = ["red", "purple", "blue", "green", "orange", "yellow"]
            cursor = turtle.Pen()
            turtle.bgcolor("black")
            for c in range(360):
                cursor.pencolor(color[c % 6])
                cursor.width(c / 100 + 1)
                cursor.forward(c)
                cursor.left(59)
            turtle.done()
        except Exception as e:
            print(f"Turtle graphics error: {e}")

# ৬. সংখ্যা প্রক্রিয়াকরণ (Number Processing)
def number_processing():
    print("\n6. NUMBER PROCESSING (EVEN & ODD):")
    print("-" * 20)
    try:
        Range = int(input("Enter number range: "))
        i = 1
        number = []
        odd = []
        even = []
        
        while i <= Range:
            number.append(i)
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
            i += 1
            
        print(f"\nAll numbers: {number}")
        print(f"Even numbers: {even}")
        print(f"Odd numbers: {odd}")
    except ValueError:
        print("Please enter a valid number!")

# ৭. ইউজার ইনপুট চেক (User Input Check)
def input_check():
    print("\n7. USER INPUT CHECK:")
    print("-" * 20)
    user = input('Enter something (or leave blank): ')
    if user == '':
        print("Input is empty (None)")
    else:
        print(f"You entered: {user}")

# ৮. স্ট্রিং ট্রিক (String Trick)
def string_trick():
    print("\n8. STRING MANIPULATION:")
    print("-" * 20)
    name = 'Hey %s, How are you?'
    friend = input('Enter your friend name: ')
    print(name % friend)

# অতিরিক্ত উদাহরণ (Additional Examples)
def additional_examples():
    print("\n9. ADDITIONAL EXAMPLES:")
    print("-" * 20)
    
    # Exception handling example
    print("Exception Handling Example:")
    try:
        num = int(input("Enter a number for division: "))
        result = 10 / num
        print(f"10 / {num} = {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Please enter a valid number.")
    
    # Person class example
    print("\nPerson Class Example:")
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            print("Hello, my name is " + self.name)
            print("My age:", self.age)

    person1 = Person("Alice", 30)
    person1.greet()
    
    # Function and loop examples
    print("\nFunction and Loop Examples:")
    def greet(name):
        print("Hello, " + name + "!")

    greet("Bob")
    
    print("Range loop:")
    for i in range(5):
        print(i, end=" ")
    print()
    
    print("While loop:")
    i = 0
    while i < 5:
        print(i, end=" ")
        i += 1
    print()

# মূল প্রোগ্রাম (Main Program)
def main():
    while True:
        print("\n" + "=" * 50)
        print("SELECT AN OPTION:")
        print("1. File Operations")
        print("2. Class and Objects")
        print("3. Basic Programming Concepts")
        print("4. Password Tracker")
        print("5. Turtle Graphics")
        print("6. Number Processing")
        print("7. User Input Check")
        print("8. String Manipulation")
        print("9. Additional Examples")
        print("10. Run All (except graphics and password tracker)")
        print("0. Exit")
        print("=" * 50)
        
        try:
            choice = int(input("Enter your choice (0-10): "))
            
            if choice == 1:
                file_operations()
            elif choice == 2:
                class_examples()
            elif choice == 3:
                basic_concepts()
            elif choice == 4:
                password_tracker()
            elif choice == 5:
                turtle_graphics()
            elif choice == 6:
                number_processing()
            elif choice == 7:
                input_check()
            elif choice == 8:
                string_trick()
            elif choice == 9:
                additional_examples()
            elif choice == 10:
                print("\nRunning all safe examples...")
                file_operations()
                class_examples()
                basic_concepts()
                number_processing()
                input_check()
                string_trick()
                additional_examples()
            elif choice == 0:
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 0-10.")
                
        except ValueError:
            print("Please enter a valid number!")
        
        input("\nPress Enter to continue...")

# প্রোগ্রাম চালু করা
if __name__ == "__main__":
    main()
