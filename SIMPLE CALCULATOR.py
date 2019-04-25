def add(x, y):
    return x + y


def subs(x, y):
    return x - y


def mult(x, y):
    return x * y


def divid(x, y):
    return x / y


def expo(x, y):
    return x**y


print("SIMPLE CALCULATOR")
print("SELECT ANAY OPERATION BAY ENTERING THE COROSPONDIN NUMBER")
print("1: ADDITION")
print("2: SUBSTRACTION")
print("3: MULTIPLICATION")
print("4: DIVITION")
print("5: EXPONENT/POWER")
print("6: EXIT")

operation = int(input("\nENTER THE OPARATION: "))
if(operation == 1):
    print("\nYOU HAVE SELECT ADDITION.")
elif(operation == 2):
    print("\nYOU HAVE SELECT SUBSTRACTION.")
elif(operation == 3):
    print("\nYOU HAVE SELECT MULTIPLICATION.")
elif(operation == 4):
    print("\nYOU HAVE SELECT DIVITION.")
elif(operation == 5):
    print("\nYOU HAVE SELECT EXPONENT/POWER.")

if(operation < 5):
    x = float(input("\n\nENTER THE FIRST VELUE: "))
    y = float(input("ENTER THE SECOND VELUE: "))

if(operation == 5):
    x = int(input("\n\nENTER THE FIRST VELUE: "))
    y = int(input("ENTER THE SECOND VELUE: "))

if operation == 1:
    print("THE SUM OF :", x, "+", y, "=", add(x, y))
elif operation == 2:
    print("\nTHE SUBSTRACTION OF :", x, "-", y, "=", subs(x, y))
elif operation == 3:
    print("\nTHE MULTIPLICATION OF :", x, "*", y, "=", mult(x, y))
elif operation == 4:
    print("\nTHE DIVITION OF :", x, "/", y, "=", divid(x, y))
elif operation == 5:
    print("\nTHE VALUE OF :", x, "^", y, "=", expo(x, y))
elif operation == 6:
    print("\nYOU HAVE CLOSE THE CALCULATOR.")
else:
    print("Please select a valid input.")
