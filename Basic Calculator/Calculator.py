#Main menu to select operation
print("Select Operation.")
print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")

#Define what each choice does
def add(x, y): return x + y
def sub(x, y): return x - y
def div(x, y): return x / y
def mul(x, y): return x * y

#Enter choice
num = '5'
choice = input("Enter option (1/2/3/4): ")
#Check if the choice is 5 or greater than exit
if choice >= num: exit()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Test each case and output
if choice == '1': print(num1, "+",  num2, "=", add(num1, num2))
elif choice == '2': print(num1, "-",  num2, "=", sub(num1, num2))
elif choice == '3': print(num1, "/",  num2, "=", div(num1, num2))
elif choice == '4': print(num1, "*",  num2, "=", mul(num1, num2))
