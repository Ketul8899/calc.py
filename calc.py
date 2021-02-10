def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    return x / y

print("Select any 1 ")
print("1.Add")
print("2.divide")
print("3.Multiply")
print("4.division")

while True:
  
    choice = input("Enter choice(1/2/3/4): ")

   
    if choice in ('1', '2', '3', '4'):
        no1 = float(input("Enter first number: "))
        no2 = float(input("Enter second number: "))

        if choice == '1':
            print(no1, "+", no2, "=", addition(no1, no2))

        elif choice == '2':
            print(no1, "-", no2, "=", subtract(no1, no2))

        elif choice == '3':
            print(no1, "*", no2, "=", multiply(no1, no2))1

        elif choice == '4':
            print(no1, "/", no2, "=", division(no1, no2))
        break
    else:
        print("Invalid Input")