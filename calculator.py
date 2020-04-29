"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
user_input = ""
index_counter = 0
list_of_operations = []

print("""NOTE: An equation is represented by an operation followed by 2 numbers, all separate by a single space.\n
    Example:\n
    + 2 3 --> Answer = 5 or,
    pow 2 3 --> Answer = 8, etc.\n""")

print("List of valid operations are: ")


list_of_operations = ["+", "-", "*", "/", "square", "cube", "pow", "mod", "q"]
 

for operation_type in list_of_operations:
    print(f"{operation_type} ")

print ("\n")

while user_input != 'q':
    user_input = input("Enter your equation > ")
    tokenized_user_input = user_input.split(" ")
    if (tokenized_user_input[0] not in list_of_operations):
         print(f"The value entered {tokenized_user_input[0]} is not valid. See the list of valid operations above and try again..")
    else:
        print ("Code further")