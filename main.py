my_name = input("enter your name: ")
my_age = int(input("enter your age: "))
print(f"My name is {my_name} and I am {my_age} years old")

num1 = int(input("enter the first number: "))
num2 = int(input("enter the secoend number:"))
operator = input("what would you like to do?")

opr = ["+", "-", "*", "/"]

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator != opr:
    print("the operation is not valid")

bus_capacity = 80
people_in = int(input("how many passengers inside the bus? "))
people_out = int(input("how many new passengers? "))
empty_seats = bus_capacity - people_in

if empty_seats > people_out:
    print(f"there are {empty_seats} avalibale seats")
elif empty_seats <= people_out:
    print("sorry the bus is full!")



