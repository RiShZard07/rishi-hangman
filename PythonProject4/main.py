import random

def math_quiz():
    """
    - prints the menu of types to Math problems to practice for the user
    - reads user choice using input()
    - generates two random int numbers a and b (random numbers between 1 and 25)
      using random module
    - chained conditional statement to provide appropriate practice for user's choice
    - checks answer and either responds by saying it was correct, or saying its wrong and
      then providing correct answer
    - when user picks an incorrect value, says its not a valid choice, and exits
      immediately through exit()
    """
    print("Welcome to Math Quiz")
    print("What are we practicing?")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division (quotient)")
    print("[5] Division (remainder)")
    choice = int(input("Choice: "))
    a = (random.randint(1, 25))
    b = (random.randint(1, 25))
    if (choice == 1):
        y = a + b
        print("what is", a, "+", b, "?")
    elif (choice == 2):
        y = a - b
        print("what is", a, "-", b, "?")
    elif (choice == 3):
        y = a * b
        print("what is", a, "*", b, "?")
    elif (choice == 4):
        y = a//b
        print("what is the quotient for", a, "/", b, "?")
    elif (choice == 5):
        y = a % b
        print("What is the remainder for", a, "/", b, "?")
    else:
        print("Not a valid choice.")

    guessed_answer = int(input(""))
    if (guessed_answer == y):
        print("That is exactly right!")
    else:
        print("Nope, it is", y)
        exit()

def main():
    """
    - main function that calls math_quiz()
    """
    math_quiz()

main()


"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 % python3 main.py
Welcome to Math Quiz
What are we practicing?
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division (quotient)
[5] Division (remainder)
Choice: 1
what is 8 + 7 ?
15
That is exactly right!
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 % 
"""

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 % python3 main.py
Welcome to Math Quiz
What are we practicing?
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division (quotient)
[5] Division (remainder)
Choice: 2
what is 22 - 22 ?
1
Nope, it is 0
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 % 
"""

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 % python3 main.py
Welcome to Math Quiz
What are we practicing?
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division (quotient)
[5] Division (remainder)
Choice: 3
what is 23 * 6 ?
138
That is exactly right!
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 %
"""

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 % python3 main.py
Welcome to Math Quiz
What are we practicing?
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division (quotient)
[5] Division (remainder)
Choice: 4
what is the quotient for 1 / 4 ?
5
Nope, it is 0
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 % 
"""

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 % python3 main.py
Welcome to Math Quiz
What are we practicing?
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division (quotient)
[5] Division (remainder)
Choice: 5
What is the remainder for 18 / 18 ?
0
That is exactly right!
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 % 
"""

"""
(.venv) rishikeshavadamarla@Rishis-MacBook-Pro-8 PythonProject4 % python3 main.py
Welcome to Math Quiz
What are we practicing?
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division (quotient)
[5] Division (remainder)
Choice: 6
Not a valid choice.
"""

