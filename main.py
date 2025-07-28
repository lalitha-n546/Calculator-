def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
while(1):
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5.Exit")


choice = input("Enter choice (1/2/3/4/5): ")

if choice== '5':
    print("Calculator exists here, Goodbye!")
    break
if choice not in("1","2","3","4"):
    print("Enter the valid input for calculation.")
    continue
try: 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

except ValueError:
        print("Invalid input! Please enter correct values.")
        continue

if choice == '1':
    print("Result:", add(num1, num2)) #Actual Parameters
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")
