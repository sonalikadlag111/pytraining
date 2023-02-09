# Calculator Program using while Loop and if-else

def add(a, b):
    return a + b


def div(a, b):
    return a / b


def mult(a, b):
    return a * b


def sub(a, b):
    return a - b


print("select ur choice")
print("1. addition is :")
print("2. division is :")
print("3. multiplication is :")
print("4. substraction is :")

while True:
    choice = input("enter your choice 1/2/3/4 :")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = int(input("enter number 1: "))
            num2 = int(input("enter number 2: "))
        except ValueError:
            print("Invalid input please Enter the right no :")

        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, '/', num2, '=', div(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', mult(num1, num2))
        elif choice == '4':
            print(num1, '-', num2, '=', sub(num1, num2))

        next_calculation = input('next calculation? (yes/no):')
        if next_calculation == "no":
            break
        else:
            print("Invalid input")
