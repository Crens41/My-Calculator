
def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a, b, c):
    answer = a - b - c
    print(str(a) + "-" + str(b) + "=" + str(answer))

def Mult(a, b):
    answer = a * b
    print(str(a) + "x" + str(b) + "=" + str(answer))

def Div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))

def squ(a):
    answer = a**2
    print(str(a) + "x" + str(a) + "=" + str(answer))

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Square")
    print("F. Exit")

    choice = input("Please select your option: ")

    if choice == "a" or choice == "A":
        print("You are performing an Addition.")
        a = int(input("insert your first number: "))
        b = int(input("insert your second number: "))
        add(a,b)
    elif choice == "b" or choice == "B":
        print("You are performing a Subtraction.")
        a = int(input("insert your first number: "))
        b = int(input("insert your second number: "))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("You are performing a Multiplication.")
        a = int(input("insert your first number: "))
        b = int(input("insert your second number: "))
        Mult(a,b)

    elif choice == "d" or choice == "D":
        print("You are performing a Division")
        a = int(input("insert your first number: "))
        b = int(input("insert your second number: "))
        Div(a,b)

    elif choice == "e" or choice == "E":
        print("You are performing a Square")
        a = int(input("insert your first number: "))
        squ(a)

    elif choice == "f" or choice == "F":
       print("Program ended")
       quit()